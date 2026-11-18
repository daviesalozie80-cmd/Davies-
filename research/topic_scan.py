#!/usr/bin/env python3
"""Weekly YouTube demand scan for GEOECONOMICS EXPLAINED.

For each search query, it pulls videos uploaded THIS MONTH (YouTube's own upload-date filter) and
reports views, the channel's subscriber count and median views, and two outlier ratios:
  views / subscribers      -> how far the topic travelled beyond the channel's audience
  views / channel median   -> how much better than that channel's normal video
A topic is a strong signal when several independent channels show high ratios on it.

Requires: pip install yt-dlp
Usage:    python3 topic_scan.py queries.txt > scan.csv      (one query per line)
"""
import csv, json, statistics, subprocess, sys, urllib.parse

THIS_MONTH = "EgIIBA%253D%253D"   # YouTube search filter: upload date = this month
THIS_WEEK = "EgIIAw%253D%253D"    # swap in for a 7-day scan

def ytdlp_json(url, limit):
    out = subprocess.run(["yt-dlp", "--flat-playlist", "-J", "--playlist-end", str(limit),
                          "--extractor-args", "youtubetab:approximate_date", url],
                         capture_output=True, text=True, timeout=300).stdout
    try:
        return json.loads(out)
    except json.JSONDecodeError:
        return {}

channel_cache = {}
def channel_stats(cid):
    if cid not in channel_cache:
        d = ytdlp_json(f"https://www.youtube.com/channel/{cid}/videos", 40)
        views = [x.get("view_count") or 0 for x in d.get("entries") or [] if x]
        channel_cache[cid] = (d.get("channel_follower_count") or 0, int(statistics.median(views)) if views else 0)
    return channel_cache[cid]

def main(path, per_query=8, window=THIS_MONTH):
    w = csv.writer(sys.stdout)
    w.writerow(["query", "title", "channel", "views", "subscribers", "channel_median", "views_per_sub", "x_channel_median", "minutes", "url"])
    for q in [l.strip() for l in open(path) if l.strip()]:
        d = ytdlp_json(f"https://www.youtube.com/results?search_query={urllib.parse.quote(q)}&sp={window}", 30)
        vids = sorted([x for x in d.get("entries") or [] if x and x.get("view_count") and x.get("channel_id")],
                      key=lambda x: -x["view_count"])[:per_query]
        for x in vids:
            subs, med = channel_stats(x["channel_id"])
            w.writerow([q, x["title"], x.get("channel"), x["view_count"], subs, med,
                        round(x["view_count"] / subs, 1) if subs else "", round(x["view_count"] / med, 1) if med else "",
                        round((x.get("duration") or 0) / 60), f"https://youtu.be/{x['id']}"])
            sys.stdout.flush()

if __name__ == "__main__":
    main(sys.argv[1])
