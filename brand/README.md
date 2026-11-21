# GEOECONOMICS EXPLAINED: Brand Kit v1.0

## Final assets (`final/`)
| File | Size | Use |
|---|---|---|
| `banner-2560x1440.png` / `.jpg` | 2560 × 1440 | YouTube banner. Upload the JPG (615 KB) or the PNG (4.97 MB); both are under YouTube's 6 MB limit. |
| `profile-1024x1024.png` / `.jpg` | 1024 × 1024 | **Main** YouTube profile picture: Marlow close-up on a clean white background (YouTube crops it to a circle). Stands out on dark-mode YouTube. |
| `profile-1024x1024-navy.png` / `.jpg` | 1024 × 1024 | Alternative: navy background with the teal globe, matching the banner. |
| `banner-black-subscribe-2560x1440.png` | 2560 × 1440 | **Banner v4 (current choice):** plain black background with a white handwritten "Subscribe" (Kalam font, SIL OFL), centred in the safe area. Rebuild with `python3 build_black.py`. |
| `banner-subscribe-2560x1440.png` / `.jpg` | 2560 × 1440 | **Banner v3:** the world-skyline background with a single large "Subscribe". 400 KB. `banner-subscribe-safe-area-guide.png` is for checking only. |
| `banner-skyline-2560x1440.png` / `.jpg` | 2560 × 1440 | **Banner v2, "world skyline" (recommended).** Light sky, landmarks of world financial and trade hubs framing the title, a container harbour, and Marlow on the quay. 459 KB. |
| `banner-skyline-safe-area-guide.png` | 2560 × 1440 | Check only: v2 with the safe-area boxes drawn on. |
| `banner-safe-area-guide.png` | 2560 × 1440 | **Checking only, don't upload.** Pink = 1546 × 423 safe area for all devices, yellow = desktop maximum, cyan = full-width tablet/desktop strip. |

All the text (channel name, tagline, red accent bar) sits inside the 1546 × 423 safe area: x 1100–2040 and y 560–833 against limits of 507–2053 and 508–931. Marlow's face is also inside it, so mobile users see the character and the name.

## Brand system
- **Character:** Marlow, drawn by the same code as `../character-system/gen.py`, so he is identical to the approved character bible. Two brand-only additions:
  - a **"confident" expression** (gently raised brows and a calm smile)
  - a **"presenting" pose** (an open arm gesturing toward the title)
- **Signature lockup:** Marlow in front of a dark-teal globe with an amber rim. The same globe appears in the banner and the profile picture, which ties the two together.

**Palette**

| Role | Colour | Hex |
|---|---|---|
| Deep navy | Background | `#0B1726` / `#10213A` |
| Dark teal | Globe | `#15444C` / `#2B6E73` |
| Warm cream | Main text | `#F2EDE4` |
| Yellow / amber | Highlights; same as Marlow's scarf | `#E0A43A` |
| Restrained red | Accent; same as his map-pin badge | `#B5473A` |

**Type**
- **Montserrat 900/800** for the wordmark.
- **Inter 500** for the tagline and supporting text.
- Both are under the SIL Open Font License and free for commercial use. The font files are in `assets/`.

**Wordmark rule:** "GEOECONOMICS" in cream, with "EXPLAINED" in amber letter-spaced to exactly the same width, and a short red bar above.

**Props** (same flat style and ink outline as the characters):
- the world map (Natural Earth data, via `world-atlas`) with shipping routes and hubs
- a cargo ship
- an oil pumpjack and barrel
- a rising/falling line chart
- faint currency symbols

## Rebuilding or editing
```
cd brand
python3 build.py                      # writes src/*.svg (banner v1 + profiles)
python3 build_skyline.py              # writes src/banner-skyline-*.svg (banner v2)
node assets/render.js src/banner-2560x1440.svg final/banner-2560x1440.png 2560 1440 1
node assets/render.js src/profile-1024x1024.svg final/profile-1024x1024.png 1024 1024 1
```
`render.js` needs Node with Playwright. The SVGs in `src/` are editable vector masters with the fonts embedded.

## Uploading
1. Go to YouTube Studio → **Customisation** → **Branding**.
2. Upload `profile-1024x1024.png` as the picture.
3. Upload `banner-2560x1440.jpg` as the banner image. Accept the default crop: the safe area is already centred.
4. Check the preview on the phone, desktop and TV tabs.
