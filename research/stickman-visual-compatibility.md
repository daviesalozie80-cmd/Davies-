# Can a 2D Stickman Style Work for Country-Economics Videos? A Compatibility Analysis

**Date:** 18 Nov 2026

**Reference clip:** a 16-second excerpt from *"The Rise of Anthropic Explained Like You're 5"*, Crayon Capital (https://youtu.be/H5GYXhpE5yI, 1.1M views).

**Supporting files in this folder**
- `reference-frames-0-8s.jpg` and `reference-frames-8-16s.jpg`: the clip sampled every 0.5 seconds.
- `crayon-capital-thumbnails.jpg`: 8 Crayon Capital thumbnails, from its top hits down to its weakest geopolitics videos.

**Evidence labels**
- **[OBSERVED]**: seen directly in the clip's frames.
- **[DATA]**: measured from YouTube public listings in my earlier research (`competitor-videos.csv`, `invisible-hand-videos.csv`).
- **[PREDICTION]**: my professional judgement. It is not proven.

**Limits of this analysis**
- The clip is **16 seconds of a 17-minute video**. I cannot judge:
  - the full video's pacing, scene variety or repetition
  - its opening hook
  - how it handles maps or data over a long runtime
  - how its ending works
- Speech-to-text was blocked in this environment, so the narration analysis uses on-screen captions and an audio loudness profile.
- I have no retention data for any channel.

---

## 1. Reference video analysis

### What happens in the 16 seconds [OBSERVED]

| Time | Shot | What it does |
|---|---|---|
| 0.0–0.5 | Wide shot: a figure from behind facing a glowing AI core in a dark server hall ("AI: WHERE SHOULD WE BEGIN?") | Mood establishing shot: cool blue, cinematic, mysterious |
| 0.5–1.0 | **Push/slide transition** (the new scene enters from the top while the old one exits) | Movement carries the cut |
| 1.0–4.0 | **Split screen**: top, a character writes "RULES" (flowchart on screen); bottom, a character carries a stack of "DATA" papers (neural-net diagram on screen) | Visual **comparison**: two approaches to AI in one frame, labelled with single words |
| 4.0–9.0 | Office wide shot: a manager points at a blackboard; the speech bubble "We'll call it this." types on. The board **types out** "GPT" → "GENERATIVE PRE-TRAINED TRANSFORMER". A third and fourth character walk in. | A jargon term is **revealed letter by letter**, synced to speech |
| 9.5–12.0 | Hard cut to a closer two-shot; caption "So what do we teach it?" … pause … "Nothing." | **Comic beat**: a set-up line and a deadpan answer, held for timing |
| 12.5–14.0 | **Punch-in close-up** of the glasses character; captions "Feed it a mountain of / books and articles, / and make it guess…" | Emphasis on the key explanation |
| 14.5–16.0 | A robot labelled "GPT" at a desk; **books pile up** while the clock hands spin | A **visual metaphor** for training: time-lapse plus accumulation |

### The style, described professionally
**"Explainer-comic 2D vector animation"**:
- Cyanide-and-Happiness-adjacent **bean-head stick figures**: big round heads, dot eyes, simple mouths, stick limbs, but clothed torsos with ties and suits.
- Set in **detailed, shaded vector environments**.
- Driven by **dialogue captions** and **diegetic labels** (words written on objects: RULES, DATA, GPT).

The animation is **limited animation**:
- Mostly static poses.
- Mouth flaps and small head and arm moves.
- Text type-on reveals.
- Camera pushes and cuts do most of the motion.

### Element by element

| Element | What I saw [OBSERVED] | Why it works or doesn't [PREDICTION] |
|---|---|---|
| **Character design** | Round heads with no outline variation, dot eyes, 1–2 line mouths. Distinguished by **hair, skin tone, glasses and clothing** (curly hair + glasses; slick hair + tie; bald; dark suit). | Instantly readable at thumbnail size. Recurring "cast" members become recognisable. Low cost per pose. |
| **Expressions** | Very limited: open mouth = talking, flat line = neutral, slight smile. No exaggerated emotion in this clip. | The deadpan look suits dry humour. It **cannot carry heavy emotion** (grief, fear) without extra devices. |
| **Movement** | Small: an arm raises to point, characters slide in, a slight bob. No walk cycles visible beyond entries. | Cheap and consistent. The risk over 17 minutes is **visual monotony**, which can't be judged from 16 seconds. |
| **Backgrounds** | Surprisingly rich: shaded server racks with cables, office walls, desks, monitors with readable diagrams, a whiteboard, chairs, a wall clock. | **This is what makes it look professional, not childish.** Simple characters on detailed sets is the key contrast. |
| **Colour** | Muted, desaturated palette: greys, beige walls, navy screens, cyan "data" glow, one accent (maroon chairs, red ties). The opening shot is cool dark blue. | Adult and calm. The cyan-on-navy screens give a "tech" identity. Nothing looks like a kids' show. |
| **Composition** | Characters placed on thirds, screens and boards as the information panel, clear foreground/background layers. | Reads like a storyboard. The eye goes from speaker to board to caption. |
| **Camera** | Push/slide transitions, cuts from wide to two-shot to close-up, a split-screen. | **Shot-size variety** creates rhythm without new art. That is cheap retention. |
| **Transitions** | One directional push (0.5s) and hard cuts. Scene detection found no hard cut above threshold for the first ~9 seconds. | Fluid, continuous storytelling. Few "PowerPoint" fades. |
| **Text and info design** | Speech-style handwritten captions; diegetic labels (RULES, DATA, DATA LEARNING); typewriter reveal of "Generative Pre-trained Transformer". | Jargon is introduced **visually as it's spoken**. This is the strongest teaching device in the clip. |
| **Props and metaphors** | A stack of paper = data. A flowchart = rules. A robot reading under a spinning clock with piling books = training over time. | Abstract concepts become **objects you can see change**. |
| **Narration** | Dialogue-led: the explanation is spoken by characters in a mini-sketch, with pauses for timing (near-silence at about 9.3s, 11s and 12s). No obvious constant music bed in the gaps. | Turns exposition into scenes. It is funny, which builds rewatch value and personality. |
| **Pacing** | A new idea or shot about every **2.5–4 seconds**; 6 distinct shots in 16 seconds. | Fast enough for the YouTube feed. Whether it holds up for 17 minutes is unknown from this clip. |
| **Consistency** | Characters are identical across shots (same hair, glasses, tie). | A disciplined model sheet, which is essential for a series. |

### Effective vs. ineffective (within this clip)
- **Effective:**
  - Concept-to-object metaphors
  - The split-screen comparison
  - Synced text reveals
  - Detailed sets that lift perceived quality
  - Humour through timing
- **Weaker or risky:**
  - Very low facial range
  - Talking-head office scenes risk repetition: three of the six shots are "people in an office"
  - Captions in a handwritten font are hard to read on mobile
  - No data visualisation in this excerpt, so whether this style can show numbers, charts and maps is unproven here

---

## 2. Niche compatibility

### The key evidence [DATA]
Crayon Capital, the source of your reference clip, has **already tested this exact niche's topics in this exact style**:

| Crayon Capital video | Views | vs channel median (468K) |
|---|---|---|
| The Wolf of Wall Street Scam ELI5 | 4.3M | 9.2× |
| The Great Depression ELI5 | 3.0M | 6.4× |
| The 2008 Financial Crisis ELI5 | 2.3M | 4.9× |
| **The Man Who Built Singapore in One Generation** | **1.2M** | 2.6× |
| The Rise of Anthropic ELI5 (your reference) | 1.1M | 2.4× |
| **Petrodollar Explained Like You're 5** | **355K** | 0.76× |
| **Xi Jinping: China's Most Powerful Leader** | **300K** | 0.64× |
| **Iran War Explained Like You're 5** | **200K** | 0.43× |
| **5000 Years of Gold** | **175K** | 0.37× |
| **The Economic Secret of WW2** | **69K** | 0.15× |

Compare the same topics on The Invisible Hand (map style):
- **Petrodollar: 603K** for The Invisible Hand vs **355K** for Crayon Capital, even though Crayon has about the same subscriber count.
- Where Crayon succeeded with a country story ("Singapore", 1.2M), it was **told through one man** (Lee Kuan Yew), not through the country as a system.

**What this shows (an inference from one channel's 35 videos, so treat it as strong evidence, not proof):**
- Stickman storytelling works best for **stories with protagonists**: a scammer, a founder, a crash with victims.
- It underperforms on **abstract country and system topics**: petrodollar, war, gold, a leader's geopolitics.
- Those abstract topics are **the core of this niche** (The Invisible Hand's top videos are about debt systems, "living in X", country decline).

### Other evidence that animated styles are accepted by this audience [DATA]
- **The Infographics Show** (cartoon characters) appeared 13 times in my niche searches, e.g. "The Next Great Recession Isn't Housing… It's FAR Dumber" at 1.85M.
- **Primate Economics** (cartoon bananas, 577K subscribers) gets 1.0–1.7M on inflation, tariffs and tax explainers.

So the economics audience **does accept cartoons**. What's unproven is cartoons as the *main* vehicle for country-macro and geopolitics.

### The questions answered
- **Does it fit the subject matter?** *Partially.* It fits stories about mechanisms, people and history. It fits poorly for geography, comparisons between countries, and statistics, which in this niche are shown on a map.
- **Will viewers accept animated storytelling?** *Yes, with conditions* (evidence above).
- **Can stickmen carry serious or complex topics?** *Complex, yes.* The GPT clip explains machine learning clearly. *Serious* (famine, war deaths, suicide, migrant hardship) is **risky**: deadpan bean-heads can read as flippant [PREDICTION].
- **Will it make content more interesting?** It adds humour and character. **It does not automatically raise retention.** Crayon's geopolitics videos underperform despite the same animation.
- **Could it reduce credibility?** Somewhat, on doom and debt topics. The "Like You're 5" branding deliberately trades authority for accessibility. Your niche's audience (sceptical, news-literate adults) clicks on **authority plus threat** ("Something's Going Seriously Wrong in France") [PREDICTION based on The Invisible Hand's title data].
- **Does it differentiate you?** **Strongly.** None of The Invisible Hand, Geography Effect, Fortune of Nations, Max Fisher, Dr. Jonathan Tam or Front Page uses character animation.
- **Short and long form?** It suits Shorts well (one gag and one concept). For long form it needs a strong system against repetition (section 5).
- **Does it fit audience expectations?** Partly. The audience expects **maps** as the visual language of countries. Removing maps removes the niche's most recognisable signal.

**Verdict:** *Pure stickman storytelling is a poor fit for this niche's core topics. A hybrid, map-first approach with stickman "explainer characters" is a strong, differentiated fit.*

---

## 3. Competitor visual comparison

| Channel | Main visuals [OBSERVED from thumbnails; DATA for performance] | How they hold interest | Weakness or opening |
|---|---|---|---|
| **The Invisible Hand** (327K) | 3D relief maps, red country, glowing arcs, B&W press photos, infographics | Map zooms, flow arcs, chart builds | No characters or human story; the visual template is fatiguing (the Japan reuse got 54K) |
| **Geography Effect** (33K, about 8 months old) | Satellite/relief maps, red highlight, white arrows | One map question per video | Faceless and impersonal; weak subscriber loyalty (330 views per subscriber) |
| **Fortune of Nations** (13K, about 1 month old) | 3D maps, red vs green countries, black-box labels | Comparison maps | Near-identical to The Invisible Hand's look, so commoditised |
| **Max Fisher** (664K) | Cinematic dark maps, news photos, archival, journalist on camera | Authority plus documentary pacing | Expensive; needs a personal brand |
| **Dr. Jonathan Tam** (161K) | AI-generated photoreal people, emotional faces | Emotional human imagery | AI-face look carries trust and suitability risk |
| **Front Page** (166K) | AI/stock dystopia, profane captions | Shock | Advertiser-unfriendly |
| **Crayon Capital** (319K) | 2D stickman comic animation | Character sketches, humour, metaphors | Geopolitics and macro topics underperform (above) |

**Advantage or disadvantage?** [PREDICTION]
- **Advantage:**
  - The *only* character-driven option in a map-saturated niche.
  - Memorable recurring characters.
  - Humour.
  - Concepts are easier to grasp.
- **Disadvantage:**
  - You lose the map signal that tells viewers "this is a serious country explainer".
  - Proven weaker on geopolitics in this exact style.
  - Higher per-minute production cost than map videos.
  - Close imitation of Crayon Capital's character design makes you a derivative of an existing 319K channel. **You must design your own characters.**

---

## 4. Audience psychology

- **Who:** mostly men aged 25–45, news-literate, financially anxious, sceptical of mainstream media (from the earlier channel analysis; an inference).
- **Realism expectations:** they don't need photorealism. They do expect *maps, data and real places* to trust a claim about a real country.
- **Educational vs. entertaining:** they come for "the real reason" (education). Humour is a bonus, not the draw. Crayon's "ELI5" framing explicitly targets a lighter, broader audience.
- **Do cartoons ease complexity?** Yes. The GPT clip turns "training on text" into a robot reading books under a spinning clock. That is the style's biggest strength.
- **Childish perception:** a real risk *if* you combine bright saturated colours, bouncy movement, goofy voices and "for kids" framing. Crayon avoids it with muted colours, detailed sets, adult themes (fraud, crashes) and dry humour [OBSERVED].
- **Memorability:** likely higher. Recurring characters and visual gags are more memorable than generic maps [PREDICTION; no retention data].
- **Trust and authority:** they drop slightly with cartoons unless you anchor claims with **real data on screen**: sourced charts, real maps, dates, and named sources in captions.

### How to look professional rather than childish
1. **Muted palette** (see section 6), with no primary-colour rainbow.
2. **Detailed, shaded backgrounds** behind simple characters.
3. **Restrained, deliberate motion.** No bouncing or squash-and-stretch gags.
4. **A calm, confident narrator.** Character voices only for short sketch lines.
5. **Real data layers**: maps, charts and numbers drawn in the same art style, with sources cited on screen.
6. **Humour as dry understatement**, never slapstick, and **never on tragedy**.
7. **Title the video with authority** ("Why Portugal Became Unaffordable"), not "Explained Like You're 5".

---

## 5. A visual storytelling and retention system

**Cadence** [PREDICTION; matches the reference clip's ~3-second shots]:
- A new shot, camera move or reveal every **3–6 seconds**.
- A new *scene type* every **30–60 seconds**.
- A deliberate **pattern interrupt every 2–3 minutes**.

### The "Map–Character–Metaphor" rotation (MCM)

| Layer | Use it when… | Example (topic: "Why Living in Portugal Became Impossible") |
|---|---|---|
| **M: Map / data scene** | Geography, comparisons, statistics, "where" | An illustrated map of Portugal; Lisbon pulses red; rent chart draws on; arrows show digital nomads arriving |
| **C: Character scene** | Human impact, decisions, dialogue, "who" | Your recurring "everyman" (a young Lisbon nurse) opens a rent letter; the landlord character shrugs |
| **M: Metaphor scene** | Abstract mechanisms, "how" | A see-saw: wages on one side, rent on the other, tipping; a bathtub filling with euros (golden visas) while the plug drains locals out |

Rotate **M → C → M → Map…** so no scene type repeats more than twice in a row.

**Characters appear for:**
- the human stakes
- decision-makers' choices, as short sketches
- the "aha" explanation moment (like "Nothing." in the reference)

**Characters leave when:**
- numbers matter
- geography matters
- the topic is tragic (switch to symbolic or illustrated stills)

**Complex information:** build it **one layer at a time**:
1. The map
2. Plus a highlight
3. Plus one number
4. Plus an arrow
5. Plus a consequence icon

Use split-screen comparisons (as at 1–4 seconds in the reference) for country A vs country B, or before vs after.

**Narration sync:**
- Cut on the stressed word.
- Type-on labels when a term is first spoken (as with "GPT" in the reference).
- Numbers count up as they're said.

**Curiosity through visuals:**
- Show the object before naming it (a locked vault, a mystery figure behind a curtain = "who is all this debt owed to?").
- Reveal it at the payoff.

**Preventing repetition:**
- Maintain a shot library of wide / medium / close-up / overhead / split-screen / map / chart / metaphor.
- Check each 2-minute block uses at least 5 of them.

**Pattern interrupts:**
- A sudden full-screen number
- A cold cut to black with one line of text
- A sketch gag
- A switch from day to night palette
- A map "zoom out to the whole planet"

**Memorable moments:**
- One **signature visual metaphor per video** (e.g. a global debt "pyramid" built of countries stacked on each other)
- Revisit it at the ending for payoff

---

## 6. Visual direction for your channel

| | Recommendation |
|---|---|
| **Keep from the reference** | Simple characters on detailed sets; diegetic labels; type-on reveals; split-screen comparisons; shot-size variety; muted palette; object metaphors; consistent model sheets |
| **Improve** | Expression range: add 6–8 standard expressions (worried, shocked, sceptical, exhausted, angry, hopeful). Use a **clean sans font for captions** (handwritten text is hard to read on phones). Add data visualisation in the same art style. |
| **Remove** | "Explained Like You're 5" framing; office-only settings; long dialogue scenes (keep exchanges to 2–3 lines) |
| **Add** | **An illustrated map system as the backbone**: flat or lightly textured country shapes in your palette, with a recurring "highlight" colour. A recurring **narrator character** (your mascot, e.g. a sceptical economist with a distinctive hat or scarf) who appears at the hook and at key reveals. On-screen source tags. |
| **Expressions** | Expressive eyebrows and mouth shapes (a stickman's face is mostly brows plus mouth). Use body language (slumped shoulders, head in hands) for serious emotion instead of exaggerated faces. |
| **Backgrounds** | Medium detail: recognisable landmarks (Lisbon trams, London terraced houses, Seoul apartment blocks) in flat-shaded vector. Background detail should never compete with the focal object. |
| **Palette** | A base of **charcoal, slate, warm off-white and muted sand**. **One danger accent** (brick red) for decline and debt, **one growth accent** (teal or green) for rising countries, and **one highlight** (amber) for key numbers. Avoid The Invisible Hand's exact red-on-teal so you don't look like a clone. |
| **Serious subjects** | No gags. Desaturate the scene, slow the camera, use silhouettes or symbolic objects (empty cribs for birth-rate collapse, closed shop shutters for recession). Characters can appear in silhouette or from behind (like the reference's opening shot). |
| **Consistency** | Build a **character bible**: front, side and back turnarounds; 8 expressions; 6 hand poses; outfits per role. Store it as PNG layers or a rigged puppet, and reuse the assets rather than re-generating each time (critical if you use AI images; see section 7). |

---

## 7. Production workflow (AI-assisted, affordable)

1. **Script to scene list:** split the script into beats of 1–2 sentences. Tag each beat **M (map/data)**, **C (character)** or **Φ (metaphor)**, with a target of about 40% maps and data, 35% characters, 25% metaphor. Use a spreadsheet with columns: beat · VO text · scene type · visual description · assets needed · camera move.
2. **Scene planning:** make quick thumbnail sketches (paper, or Excalidraw, free) for each beat. Mark the "money shot" per section.
3. **Character and environment design:** design your cast **once**, in vector, so they stay consistent. Use Inkscape (free), Affinity Designer (~$70 one-off) or Adobe Illustrator. Optionally generate initial concepts with an AI image model, then **redraw and lock them as vector assets**.
4. **Image generation:**
   - **Backgrounds and metaphor props:** AI image tools (Ideogram, Leonardo, Midjourney, ChatGPT/Gemini image models) work well with a fixed style prompt and reference image. Re-colour them to your palette in Photopea (free).
   - **Characters:** reuse your vector puppet rather than regenerating. AI is poor at keeping stickman identities consistent across hundreds of shots.
   - **Maps:** Natural Earth / QGIS (free), or MapChart.net, exported as SVG and styled in your palette.
   - **Charts:** Flourish or Datawrapper (free), restyled.
5. **Animation:**
   - **Limited puppet animation** (mouths, arms, blinks, entrances) in **Adobe Animate**, **Moho** (~$60), **Cartoon Animator 5**, or free in **Blender Grease Pencil** or **OpenToonz**.
   - **Text reveals and motion graphics** in **After Effects** or free **DaVinci Resolve Fusion**.
   - AI image-to-video tools (Kling, Runway, Pika, Hailuo) can animate one-off background shots (a spinning clock, falling coins). Expect style drift; use them sparingly.
6. **Camera:** slow push-ins (2–5% scale over the shot), pans across wide sets, punch-in close-ups for emphasis, map zoom from globe to country.
7. **Transitions:** directional push/slide (as in the reference), match-cuts (a coin becomes the sun), map zoom-throughs. Avoid dissolves and flashy preset transitions.
8. **Voiceover:** your own voice, recorded first. Clean it in Audacity or Adobe Podcast Enhance (free). Cut visuals to the waveform. Use CapCut's or Resolve's auto-captions for timing, then restyle them.
9. **Sound:** a light ambient music bed (YouTube Audio Library free; Epidemic Sound or Artlist paid). SFX for every reveal: whoosh, pop, typewriter, paper, cash register (Pixabay or Freesound, check licences). The reference uses silence for comic timing, so keep that device.
10. **Final edit:** CapCut Desktop or DaVinci Resolve (free). Build the timeline in VO order and drop in assets. Do a "boring check": scrub at 2× speed and flag any 8+ seconds without visual change.

### Which scene type for which beat

| Beat type | Visual |
|---|---|
| Hook / shocking fact | Character reacts plus a big number, or a dramatic map pulse |
| Where / geography / migration / trade | **Map** |
| How much / trends | **Chart** in house style |
| Who decided / conflict | **Character sketch** (2–3 lines) |
| How a mechanism works | **Metaphor scene** |
| Human cost | **Character** (quiet, no gags) or symbolic still |
| Historical context | **Illustrated stills** with slow pans (cheaper than animation) |
| Payoff / conclusion | Return to the signature metaphor plus a map |

**Realistic effort** [PREDICTION]: once your asset library exists, a 15-minute hybrid video takes about 30–45 hours solo. That is roughly 1.5× a pure map video. The first 3 videos will be slower while you build the cast, sets and map kit.

---

## 8. Three presentation strategies

| | **A. Pure stickman** | **B. Stickman + maps, objects, diagrams** | **C. Hybrid documentary animation** |
|---|---|---|---|
| Description | Everything is character sketches in illustrated sets (like the reference clip) | Characters as guides inside an illustrated world of maps, charts and metaphors, all in one art style | B plus cinematic illustrated stills, infographics and **occasional real footage or photos** (archival, news photos, real places) |
| Niche fit | Low: no maps, weak on country topics (Crayon's geopolitics median shows this) | **High** | High |
| Credibility | Lowest | Good (data and maps in style) | Highest (real-world anchors) |
| Differentiation | High | **High** (no competitor does this) | Medium-high (photo moments resemble competitors) |
| Cost and time | Medium-high (lots of character animation) | Medium | Highest (licensing plus style integration) |
| Copyright risk | Low | Low | Medium (photos and footage need licences or fair-use discipline) |
| Consistency risk | Low | Low | Medium (mixed media can look messy) |
| Scalability | Medium | **High** (reusable map kit, cast and props) | Medium |

**Recommendation: B, with a small amount of C.** Use B as the house style. Add C's real imagery only for **proof moments**: a headline, a real document, a real photo of a place. Use it 3–6 times per video, framed inside your illustrated style (e.g. a photo pinned to an illustrated corkboard, as in Crayon's Xi thumbnail).

---

## 9. Monetization and professionalism

**No art style guarantees or prevents monetization.** The relevant YouTube policies are about **originality and added value**, not drawing style.

| Risk | Where it applies to you | Mitigation |
|---|---|---|
| **Repetitive / mass-produced content** (inauthentic content policy) | Templated AI images, an AI voice, recycled scripts, and identical structures across many uploads could look mass-produced | Original scripts with real research; your own voice; unique metaphors per video; varied structures |
| **Reused content** | News clips, other creators' footage, unmodified stock | Use real footage only briefly, transformed, with commentary; prefer your own illustrations |
| **Copyright** | **Copying Crayon Capital's character design or scenes**; AI images that imitate a recognisable style; music | Design an original cast; don't prompt AI with another channel's name or style; licence music |
| **Advertiser suitability** | War, migration, suicide and violence topics (yellow icons possible); cartoon depictions of violence | Non-graphic depiction; neutral, factual language; no gore or slurs; keep humour away from tragedy |
| **Made-for-kids misclassification** | Cartoon style plus "Explained Like You're 5" framing | Mark it "not made for kids", write adult topics and titles, use no child-targeted elements. Under COPPA, a kids designation removes personalised ads and comments. |
| **Audience trust** | Cartoon plus doom can feel like entertainment, not information | Cite sources on screen and in the description; show real data; correct errors publicly |

**How to make the videos clearly original and valuable:**
- Your own thesis per topic
- Primary data sources (IMF, OECD, national statistics offices)
- Custom metaphors
- A consistent original cast
- Your own narration
- A "what this means for you" payoff that no competitor offers

---

## 10. Scorecard

### Score for the reference style as-is (pure stickman, like the clip)

| Area | Score | Reason |
|---|---|---|
| Niche compatibility | **4/10** | Proven on finance and people stories, but under the source channel's own median on geopolitics and macro (Petrodollar 0.76×, Iran 0.43×, WW2 0.15×). No maps. |
| Audience acceptance | **6/10** | Cartoons are accepted in economics (The Infographics Show, Primate Economics, Crayon), but less so for serious country decline |
| Professional appearance | **7/10** | Detailed sets, a muted palette and a consistent cast look polished. Limited expressions and a handwritten caption font hold it back. |
| Storytelling potential | **8/10** | Excellent at turning abstractions into scenes and gags (the GPT reveal, the robot training metaphor) |
| Retention potential | **6/10** | Strong shot variety in 16 seconds; whether it holds 15–20 minutes without repetition can't be judged |
| Differentiation | **8/10** | No direct niche competitor uses character animation |
| Long-form suitability | **5/10** | Risk of office-sketch monotony without maps and data scenes |
| Production affordability | **5/10** | Character animation is the most time-consuming part. Fine once assets exist, slow at the start |
| Scalability | **6/10** | Reusable cast helps; each new country needs new sets |
| Monetization suitability | **6/10** | Fine if marked "not for kids" and kept non-graphic. "Explain like 5" framing and cartoon violence raise risks |
| **Total** | **61/100** | |

### Score for the recommended hybrid (Strategy B + C)
Niche fit 8, acceptance 7, professionalism 8, storytelling 9, retention 7, differentiation 8, long form 8, affordability 5, scalability 7, monetization 7 = **74/100** [PREDICTION]

---

## 11. Final verdict

1. **Should I use this visual style for this niche?**
   - **Not as-is.** Pure stickman sketches fit people-and-company finance stories (Crayon's sweet spot), not this niche's core: country and system topics.
   - **Yes, as an ingredient** of a map-first hybrid.
2. **Can 2D stickmen compete against documentary visuals?** In a hybrid, yes, and they would be the only character-led option in the niche. Alone, the best available evidence says they compete **worse** on geopolitics and macro topics: Crayon's Petrodollar got 355K vs The Invisible Hand's 603K.
3. **Biggest advantages:**
   - Differentiation
   - Clarity of abstract mechanisms through metaphor
   - Humour and personality
   - A recognisable recurring cast
   - Low copyright risk
   - Works in Shorts
4. **Biggest disadvantages:**
   - Weaker credibility on serious doom topics
   - Loses the niche's map signal
   - Character animation is slower to produce
   - A potential "childish" or "made for kids" perception
   - Easy to look derivative of Crayon Capital
5. **What would make it more professional?**
   - Muted palette plus detailed sets
   - An illustrated map and data system in the same style
   - Clean caption typography
   - Restrained motion
   - A calm authoritative narrator
   - On-screen sources
   - No "ELI5" framing
   - No jokes on tragedy
6. **Pure or hybrid?** **Hybrid.**
7. **My recommended format:** "**Illustrated map documentaries with a recurring cast**":
   - 14–18 minutes
   - About 40% illustrated maps and data, 35% character scenes, 25% metaphor scenes
   - Real photo or document inserts at proof moments
   - One original mascot narrator
   - Titles with authority, not "explained like you're 5"
8. **Would I confidently build a channel on it?**
   - **Pure stickman version:** no. The closest real-world test (Crayon on geopolitics) underperformed.
   - **Hybrid version:** yes, with moderate confidence. It combines the niche's proven demand and map language with a visual identity no competitor owns.

   **Two tests before committing to a series:**
   1. **Produce 3 pilots:**
      - one person-led country story (like Crayon's 1.2M Singapore)
      - one system mystery ("If every country is in debt…")
      - one "living in X became impossible"
   2. **Compare impressions click-through rate and average view duration** against your expectations after 2 weeks each, and keep whichever format wins.

### Sources
- Reference clip (uploaded) and the YouTube public listings in `competitor-videos.csv`. Crayon Capital's video list was collected 17 Nov 2026 from https://www.youtube.com/channel/UCP9RPj_BG0vit2TNM7LuRxA.
- Earlier reports in this folder: `the-invisible-hand-channel-analysis.md`, `new-competitor-channels.md`.
