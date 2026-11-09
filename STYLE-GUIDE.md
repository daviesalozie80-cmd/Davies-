# Visual Style Guide — Stick-Figure Explainer

This guide comes from the 15 reference frames in `assets/reference/`. Use it so every new
frame matches them, whether you draw it, animate it, or generate it with an image model.

## 1. The look in one sentence
Flat, hand-inked 2D cartoon on warm cream paper: one simple idea per frame, a white round-headed
stick figure, a few muted accent colours, and one bold uppercase label.

## 2. Canvas
| Setting | Value |
|---|---|
| Aspect | 16:9 (references are 1376×768; export video at 1920×1080) |
| Default background | Warm cream paper `#F5EEDC`, faint paper grain |
| Alt "clean" background | Off-white `#F7F6F1` (charts, stopwatches, maps) |
| Safe area | Keep the bottom ~10% and the bottom-right box (~15% wide) empty. Several references have a cream bar and box there, used for subtitles or a logo. |
| Composition | One main subject, centred or on a third, with lots of empty space. No busy backgrounds. |

## 3. Palette (sampled from the references)
| Role | Hex | Used for |
|---|---|---|
| Paper | `#F5EEDC` | Main background |
| Ink | `#1A1A1A` | All outlines, stick bodies |
| Charcoal | `#3A3A3A` | Text labels, scales, metal objects |
| Brick red (main accent) | `#B95545` | Arrows, highlights, the "heavy" or "bad" thing, map dots |
| Sage green | `#8E9470` | Progress bars, feathers, trees, the "light" or "good" thing |
| Dusty blue | `#B1BFCC` | Cold areas, radius circles, magnifier lenses |
| Fire orange | `#F2A541` → `#E8642C` | The campfire (recurring motif) |
| Modern teal sky | `#B7FBF0` | "TODAY" / modern-city scenes |
| Daytime sky | `#CDECFE` | Outdoor past scenes (savanna, mountains) |
| Night navy | `#0E1525` → `#1C2536` | Night or anxiety scenes, with a cool phone glow |
| Spotlight gold | `#F3D9A6` | Singling someone out |
| Neutral grey | `#9C9C9E` | "Crowd / conformity" backgrounds |

Rule: at most **one accent colour plus fire** per frame. Red means emphasis.

## 4. The main character
See `assets/reference/10-base-character.webp`.
- **Head:** big, perfect white circle (about 1/4 of body height) with a thick black outline (~6 px at 1080p).
- **Face:** two black dot eyes, small curved eyebrows that carry the emotion, a tiny line or "o" for the mouth. No nose, ears or hair by default.
- **Body:** a single thin black line (~3 px). Limbs are smooth curved lines. Hands and feet are small white circles or ovals with outlines.
- **Costumes go over the body, never replace it:** fur tunic and shaggy hair or beard for ancient humans, a khaki shirt with a pith hat and round glasses for the anthropologist.
- **Emotions:** worried (brows up and in), skeptical (one brow raised), surprised (an "o" mouth), smug (a crooked smile, closed-arc eyes), sad (a wobbly mouth, tear lines).
- **Crowds:** tiny brown or grey stick figures with no faces (see the circle around the fire in `02`).

## 5. Recurring objects and icons
- **Campfire:** orange flame on grey logs and stones, with a soft glow. This is the show's symbol, so put it in thought bubbles, magnifiers and map centres.
- **Balance scale:** charcoal, with a red rock for "heavy" and a green feather for "light".
- **Stopwatch:** red, with a big number on its face.
- **Progress bar:** sage green with a small red end and a red pointer arrow.
- **Maps:** thin black outlines on cream, red dots, thin arcs between places, small tree or landmark icons.
- **Arrows:** fat brick-red arrows with a solid triangular head.
- **Labels:** small hand-drawn calendars, moons with stars, snowflakes for cold, and a dark cloud for a bad mood.

## 6. Typography
- Bold, condensed, rounded sans in **ALL CAPS**, charcoal `#3A3A3A`. Close free fonts: **Bebas Neue** or **Oswald Bold** for big numbers, **Patrick Hand SC** or **Gochi Hand** for the hand-lettered captions ("THE WEIRD ONE", "2 A.M.").
- One label per frame, two at most. Big numbers (`50 KM`, `99.8%`, `18 MINUTES`) are the hero of their frame.
- Proofread labels. Reference `12` reads "18 MINUTES TOTAL **TOTAL**" (a duplicated word). Generated text often goes wrong like this.

## 7. Motion (how channels like this animate)
- Mostly still frames with a slow zoom or pan (about 105% over the shot).
- Pop-ins: objects scale from 0 → 110% → 100% in about 8 frames. Labels type on or fade in.
- Arrows "draw" from the tail to the head. Map arcs draw along their path. Bars fill from left to right.
- A blink or small head-tilt loop on the character keeps it alive.
- Cut on every new sentence, so each frame lasts about 3–6 s. That means roughly 12–15 frames per minute of narration.
- Sound: a soft paper or whoosh sound on transitions, a pop on pop-ins, and a quiet acoustic or lo-fi bed under the narration.

## 8. Image-generation prompt template
Paste this prefix before every scene description:

```
Flat 2D hand-drawn cartoon explainer illustration, 16:9. Warm cream paper background (#F5EEDC)
with subtle paper texture. Clean thick black ink outlines, flat muted colours, minimal shading.
Characters are simple stick figures with a large perfect white circle head, black dot eyes,
small expressive eyebrows, tiny mouth, single thin black line body and limbs, small round
white hands and feet. Muted palette: brick red #B95545 accent, sage green #8E9470, dusty blue
#B1BFCC, charcoal #3A3A3A. Lots of empty space, one clear subject. Keep bottom 10% empty.
Scene:
```

Negative prompt (if your tool supports one):
`photorealistic, 3D, gradients, anime, detailed faces, noses, realistic hands, clutter, busy background, watermark, misspelled text, extra limbs`

**Tip:** Text from image models is often wrong. Generate frames *without* labels, then add the text
in your editor (CapCut, DaVinci Resolve, After Effects) with the fonts above.
