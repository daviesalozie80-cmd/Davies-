# Character Bible: Original Cast for a Global-Economics Explainer Channel

**Version 1.0 · 18 Nov 2026**

**Visual sheets in this folder**
- `png/01-marlow-turnaround.png`: front, three-quarter, side and back views, plus proportion guides.
- `png/02-marlow-expressions.png`: 15 expressions.
- `png/03-marlow-poses.png`: 15 poses.
- `png/04-cast-lineup.png`: the full cast side by side.
- `png/05-supporting-cast.png`: supporting characters with views, expressions and colour swatches.
- `png/06-palette.png`: the colour system.

**Source files**
- `sheets/*.svg`: editable vector originals. Open them in Inkscape, Illustrator or Figma.
- `gen.py`: the generator. Every sheet is built from **one parametric skeleton**, so proportions cannot drift. Change a colour or feature there and re-run `python3 gen.py`.
- `character-bible.html`: all sheets on one page.

---

## 1. The niche the characters must serve

| | |
|---|---|
| Niche | Global economics × geopolitics, told country by country |
| Sub-niches | Why living in X became unaffordable; debt and money systems; rising vs declining nations; how one decision changed a country |
| Audience | Mostly men aged 22–45 in the UK, US, Europe and Australia. News-literate, financially anxious, sceptical. They want "the real reason". |
| Tone | **Documentary-serious with dry wit.** Calm authority, clear explanation, occasional understated humour. Never slapstick, never childish, never a joke about suffering. |
| Emotional range needed | Concern, scepticism, revelation ("so that's why"), quiet determination, occasional dark irony |
| Character job | Make abstract systems *human*: who decides, who pays, who profits, who explains. The maps and charts carry the data; the characters carry the stakes. (This follows the hybrid "map-first + cast" format recommended in `stickman-visual-compatibility.md`.) |

**Verdict on tone:** the characters should be **educational and documentary, with restrained humour**, not cartoon-comedic.

---

## 2. What I took from the reference video (the visual language)

These were measured from full-resolution frames of the reference clip.

| Feature | Reference observation | Our rule |
|---|---|---|
| Head | Large circle, about ⅓ of body height | Circle ⌀96u in a figure about 286u tall (≈ ⅓) |
| Body | Capsule/bean torso, about the same width as the head | Rounded rectangle 84u × 130u, corner radius 38. Head = 1.14× torso width |
| Limbs | Single thin black lines with rounded ends, no hands or feet | Stick limbs 4.2u wide with round caps. Arms start at the torso sides. **No hands, no feet.** |
| Face | Small vertical oval eyes, no highlights; thin arc brows; one-line mouth; no nose | Same eye and mouth language. **Our signature change: thick rounded-bar brows** (the main expressive feature) |
| Hair | A flat solid shape sitting on the head, with a wavy lower edge | Same technique, original shapes (see each character) |
| Clothing | Flat torso colour, a collar or tie as the only detail, trousers as a dark band at the base | Same: outfit = torso colour + 1–3 simple details + trousers band |
| Outline | Uniform dark outline, about 0.5% of frame height, rounded joins | Uniform 2.8u outline in `#1E1F22` (never pure black) |
| Shading | One flat darker crescent (bottom-right of the head, one side of the torso), no gradients | Two-tone cel shade: the shade colour offset from top-left light. No gradients, no texture. |
| Palette | Muted greys, beige, navy, one maroon accent | Muted base + one accent per meaning (section 5) |
| Shadow | Soft grey ellipse under the feet | Black ellipse at 14% opacity |
| Complexity | Very low on characters, medium detail on backgrounds | Same. Characters stay simple; detail lives in sets and maps. |

**What we deliberately did NOT copy:** the reference channel's specific cast (curly hair + rectangular glasses; slick hair + red tie in a white shirt; the bald man with a grey patch), its white-shirt office uniform, and its thin brows. Our cast uses different hair silhouettes, outfits, brow design and a signature scarf. That makes it recognisable as its own universe.

---

## 3. Main character: MARLOW (Guide and narrator)

**Concept:** Marlow is the channel's on-screen guide. He is a sceptical, well-travelled economic explainer who "goes and looks" at each country.
- He appears at the **hook**, at each **major reveal**, and in the **payoff**.
- He reacts to data on behalf of the viewer.
- He is curious and calmly sceptical, not goofy.

**Silhouette test:** in solid black, you can still recognise him by:
1. The **upward hair swoop** curling to his right.
2. The **scarf tail** hanging on his left chest.
3. The coat's long capsule body.

**Brand tie-ins:**
- His **amber scarf** is the channel's highlight colour. It should match the amber used on key numbers in charts.
- The **brick-red map-pin badge** on his lapel is the channel's logo motif.

### MASTER DESCRIPTION: MARLOW (copy exactly, every time)
> Marlow, an original 2D flat vector cartoon man in a minimal bean-body stickman style. A large perfectly round head about one third of his total height, warm light-tan skin (#EBC9A4) with a flat darker crescent shade at the lower right (#D3AC84). Dark chestnut-brown hair (#4A3426) as a smooth solid cap with a gently wavy hairline and **one tall swooping tuft rising from the top centre and curling to his right**. Small solid black vertical oval eyes, **thick short rounded-bar black eyebrows**, a single thin line mouth, no nose, no ears visible from the front. Body is a rounded capsule-shaped torso slightly narrower than the head, wearing a **deep navy overcoat (#2F3B52)** with a narrow off-white shirt V at the neck, a thin centre seam and two small black buttons. A **mustard-amber knit scarf (#E0A43A)** wraps the neck as a rounded band, **with one tail hanging down the left side of his chest ending in a short fringe**. A tiny **brick-red map-pin badge (#B5473A)** on the right lapel. Charcoal trousers shown only as a dark band at the base of the torso. Arms and legs are single thin dark lines with rounded ends, **no hands and no feet**. Uniform dark-charcoal outline (#1E1F22), flat two-tone cel shading, no gradients, no texture.

---

## 4. Supporting cast (each has one storytelling job)

| Character | Storytelling job | Silhouette key | Never |
|---|---|---|---|
| **Rosa**, Everyday Citizen | The person who *pays*: renter, commuter, nurse, shopper, emigrant, taxpayer. Carries the human stakes in "living in X became impossible" stories. | High round **hair bun** + teal hoodie | Never a caricature of any nationality; country is shown by setting and props, not by changing her |
| **Dr. Vera Lind**, The Expert | Explains data, research and institutions (central banks, the IMF, statistics offices). The "evidence" voice. | **Grey straight bob with a blunt fringe** + round glasses + lanyard badge | Never used as a stand-in for a real named economist |
| **The Minister**, The Leader | Any government decision-maker: prime minister, president, finance minister. Country is shown by **tie colour + lapel flag pin**. | Neat **side-part hair** + charcoal suit + coloured tie | Never a likeness caricature of a real politician (see section 8, rule R7) |
| **Mr. Ledger**, The Creditor | Capital and creditors: banks, bondholders, landlords, corporations, "who is the money owed to". | **Bald with a shine mark** + small moustache + black suit + gold tie + gold pocket square | Never coded to any ethnicity or religion; he represents an *institution*, not a group of people |
| **Dev**, The Worker | Labour and industry: factories, ports, farms, construction, strikes, jobs moving overseas. | **Yellow hard hat** + orange hi-vis vest with silver stripes | Swap the hard hat for a flat cap or headscarf for other jobs; keep the vest *colour* |
| **The Commons**, Crowd system | Populations, voters, migrants, statistics ("1 in 6 people…"). Faceless figures in 3–5 slate-grey tints; **one highlighted in brick red** = "this one is you / the affected share". | Faceless round head + plain torso | Never given faces, unless one steps forward to become Rosa or Dev |

**Historical figures (a kit, not new characters):** use **The Minister** or **The Commons** body plus a period costume overlay:
- 19th-century industrialist: top hat, tailcoat tails
- Monarch: crown, sash
- WWII-era official: peaked cap
- Ancient ruler: laurel wreath

Each gets a **name caption on screen**. Keep the base proportions untouched.

**Opposing characters** are not a separate cast. "Opposition" is a *role* any of them can play: Mr. Ledger vs Rosa, Minister vs Minister (two tie colours), Dev vs Mr. Ledger.

### MASTER DESCRIPTIONS (append to the shared style block in section 7)
- **Rosa:** Rosa, an original 2D flat vector cartoon woman in the same minimal bean-body stickman style. Large round head, medium-brown skin (#B98058) with a flat darker crescent shade (#9E6844). Near-black hair (#2A1E1A) as a smooth cap with a **high round bun on top**. Small black oval eyes, short dark bar eyebrows, a thin line mouth, no nose. Wears a **muted teal hoodie (#3E8E85)** with a darker hood collar band around the neck, two off-white drawstrings and a front pocket, and dark slate trousers as a band at the base. Thin line arms and legs, no hands, no feet.
- **Dr. Vera Lind:** Dr. Vera Lind, an original 2D flat vector cartoon woman in the same minimal bean-body stickman style. Large round head, fair skin (#F1D4BD). **Light silver-grey straight bob haircut with a blunt fringe** covering the sides of the head to jaw level. **Thin round black-rimmed glasses.** Small black oval eyes, short thin dark brows, a thin line mouth. Wears a **mid-grey cardigan (#8A8F98)** open over a white blouse, two small buttons, and a **teal lanyard with a small white ID badge**. Dark trousers band. Thin line limbs, no hands, no feet.
- **The Minister:** The Minister, an original 2D flat vector cartoon politician in the same minimal bean-body stickman style. Large round head, light-tan skin (#E3BE9A). **Neat dark-grey hair (#55575C) with a side parting**. Small black oval eyes, short dark brows, a thin line mouth. **Charcoal suit (#3A3D44)**, white shirt V, a **narrow tie in [COUNTRY COLOUR]**, a tiny rectangular flag pin on the right lapel, and a dark trousers band. Thin line limbs, no hands, no feet.
- **Mr. Ledger:** Mr. Ledger, an original 2D flat vector cartoon financier in the same minimal bean-body stickman style. **Bald, perfectly round head** with fair skin (#F0CDAE) and a small white shine mark on the upper left. **A small neat grey-brown moustache.** Small black oval eyes, short dark brows, a slight knowing smile. **Near-black suit (#25262B)**, white shirt V, a **gold tie (#C9A24A)** and a gold pocket-square triangle. Thin line limbs, no hands, no feet.
- **Dev:** Dev, an original 2D flat vector cartoon worker in the same minimal bean-body stickman style. Large round head, warm brown skin (#C99470). **A yellow-amber hard hat (#E0A43A)** with a centre ridge and a wide brim. Small black oval eyes, short dark brows, a thin line mouth. Wears a **bright orange hi-vis vest (#E07B39) with two horizontal silver reflective stripes** over a slate-blue shirt, and a dark trousers band. Thin line limbs, no hands, no feet.
- **The Commons:** a crowd of identical faceless figures in the same minimal bean-body stickman style. Plain round heads and plain capsule torsos in muted slate-grey tints (#AEB6C0, #9AA3AE, #7D8794, #5B6573), no facial features, no hair, thin line limbs. Optionally one figure highlighted in brick red (#B5473A).

---

## 5. Colour palette

| Use | Colour | Hex |
|---|---|---|
| Outline and limbs | Ink | `#1E1F22` |
| Scene base | Charcoal / Slate / Off-white / Sand | `#2B2E33` `#5B6573` `#F2EDE4` `#D8C7A8` |
| **Meaning accents (identical in maps and charts)** | Brick red = decline, debt, danger · Teal = growth, recovery · Amber = highlight, key number, Marlow's scarf | `#B5473A` `#3E8E85` `#E0A43A` |
| Marlow | Skin / shade / hair / coat / coat shade / shirt / scarf / scarf shade / trousers / pin | `#EBC9A4` `#D3AC84` `#4A3426` `#2F3B52` `#243046` `#ECE7DD` `#E0A43A` `#C08926` `#2B2B2E` `#B5473A` |
| Mouth interior | Dark red-brown | `#4A2A27` |

The full per-character swatches are in `png/05-supporting-cast.png`.

**Rule:** a character's clothing colour must never be brick red or teal unless it carries that meaning. Rosa's teal hoodie is the one exception: she is the "person who could recover".

---

## 6. Expression and pose libraries

**Expressions** (`png/02-marlow-expressions.png`): neutral, happy, sad, angry, surprised, shocked, confused, worried, fearful, excited, serious, thinking, determined, suspicious, disappointed.
- **Only three parts may change:** brows (angle and height), eyes (shape) and mouth (shape).
- **Allowed extras:**
  - sweat drop (worried, fearful)
  - "?" (confused)
  - shock lines (shocked)
  - sparkles (excited)
  - thought dots (thinking)
- **Default channel register:** neutral, serious, thinking, suspicious, worried and determined cover about 80% of scenes. Use the "big" emotions (shocked, excited, fearful) only at reveals.

**Poses** (`png/03-marlow-poses.png`): standing, walking, running, sitting, pointing, explaining, thinking, looking back, holding an object, reading a document, working at a laptop, arguing, celebrating, falling, reacting.
- All poses use the same torso and head size.
- Only the **limb lines**, a **body lean (≤ 15°)** or a **whole-body rotation** (falling only) change.

---

## 7. AI image-generation prompts

### How to get consistent results (read first)
1. **Always attach a reference image:** the turnaround PNG plus the expression sheet. Use the tool's character- or style-reference feature: Midjourney `--cref`/`--sref`, Ideogram or Leonardo character reference, ChatGPT or Gemini image editing with an uploaded image. Text alone will drift.
2. **Paste the STYLE BLOCK, then the character's MASTER DESCRIPTION, then the scene.**
3. **Best practice for a long series:** AI tools cannot hold a stickman's exact identity across hundreds of shots.
   - **Use AI for backgrounds, props and one-off scenes.**
   - **Use the vector character files in `sheets/` as puppets.** Place them, swap expressions and pose the limbs in your animation or editing tool.
   - This is how you guarantee consistency for years.

### STYLE BLOCK (prefix every prompt)
> Flat 2D vector cartoon illustration, minimal explainer-animation style. Bean-body stickman characters: large perfectly round heads about one third of body height, rounded capsule torsos, single thin dark line arms and legs with rounded ends, no hands, no feet. Small solid black oval eyes, simple line mouths, no noses. Uniform dark charcoal outlines, flat two-tone cel shading (one darker crescent shade), no gradients, no textures, no 3D. Muted adult colour palette of charcoal, slate grey, warm off-white and sand, with accents of brick red, teal and amber. Clean, calm documentary mood, 16:9 composition.

### Ready-to-use character prompts (reference sheet or turnaround)
- **Marlow sheet:** `[STYLE BLOCK] Character reference sheet of [MARLOW MASTER DESCRIPTION]. Four full-body views in a row: front, three-quarter, side profile, back, all identical proportions, neutral expression, standing straight with arms relaxed. Plain warm off-white background (#F2EDE4), soft grey ellipse shadows under each figure.`
- **Rosa:** `[STYLE BLOCK] Full-body character turnaround of [ROSA MASTER DESCRIPTION], front, three-quarter, side and back views, plain off-white background.`
- **Dr. Vera Lind:** `[STYLE BLOCK] Full-body character turnaround of [VERA MASTER DESCRIPTION] holding a clipboard, front, three-quarter, side and back views, plain off-white background.`
- **The Minister:** `[STYLE BLOCK] Full-body character turnaround of [MINISTER MASTER DESCRIPTION], tie colour [e.g. deep red], front, three-quarter, side and back views, plain off-white background.`
- **Mr. Ledger:** `[STYLE BLOCK] Full-body character turnaround of [LEDGER MASTER DESCRIPTION] holding a black briefcase, front, three-quarter, side and back views, plain off-white background.`
- **Dev:** `[STYLE BLOCK] Full-body character turnaround of [DEV MASTER DESCRIPTION], front, three-quarter, side and back views, plain off-white background.`
- **The Commons:** `[STYLE BLOCK] A crowd of [N] [COMMONS MASTER DESCRIPTION] standing in loose rows, one figure highlighted in brick red, plain off-white background.`

### Reusable SCENE TEMPLATE
```
[STYLE BLOCK]
CHARACTER(S): [paste MASTER DESCRIPTION for each character in shot]
EXPRESSION: [one of the 15 library expressions] — change only eyebrows, eyes and mouth.
POSE: [one of the 15 library poses, or describe limb lines] — keep head and torso size identical.
SETTING: [specific place, e.g. "a narrow Lisbon street with yellow tram, tiled facades and 'For Rent €2,400' signs"], simplified flat vector, medium detail, muted palette, background less detailed than characters' outlines.
DATA / OBJECTS: [e.g. "a large rent chart rising in brick red on a billboard", "a stack of euro banknotes"] in the same flat style.
CAMERA: [wide / medium / close-up / over-the-shoulder / overhead], eye level, 16:9.
MOOD & LIGHT: [e.g. "late afternoon, warm but slightly desaturated, serious documentary tone"].
TEXT: none (captions are added in editing).
```

**Worked example:**
```
[STYLE BLOCK] CHARACTER: [MARLOW MASTER DESCRIPTION] and [ROSA MASTER DESCRIPTION].
EXPRESSION: Marlow suspicious, Rosa worried. POSE: Marlow pointing at a sign, Rosa holding a letter.
SETTING: narrow Lisbon street, yellow tram, tiled facades, estate-agent window with rental listings.
DATA: one listing enlarged showing a high rent number highlighted in amber.
CAMERA: medium shot, eye level, 16:9. MOOD: overcast, muted, serious. TEXT: none.
```

### NEGATIVE PROMPT (append to every prompt, or put in the negative field)
> 3D, CGI, render, realistic, photorealistic, anime, manga, chibi, kawaii, Pixar style, Disney style, clay, plush, gradient shading, airbrush, glossy, soft lighting bloom, texture, paper grain, watercolor, sketchy lines, inconsistent outline thickness, thick black hands, fingers, gloves, feet, shoes, toes, detailed anatomy, muscles, realistic face, nose, nostrils, ears from front view, eyelashes, eye highlights, eye whites (unless shocked), teeth (unless gritting), blush stickers, neon colors, oversaturated, rainbow palette, childish, nursery, toddler, cute baby proportions, extra limbs, extra fingers, distorted head, oval or egg-shaped head, tiny head, long neck, visible neck, watermark, logo, signature, text, letters, speech bubbles, caption, frame border, real politician likeness, celebrity likeness, brand logos, copyrighted characters.

---

## 8. Permanent consistency rules

**Fixed for every character, forever (must never change)**
- **F1** Head is a perfect circle, ⌀96u. Body height to head top is about 286u (≈ 3 heads). Head width = 1.14× torso width.
- **F2** Torso is a rounded capsule, 84u × 130u, corner radius 38u. The head overlaps the torso top by about 15u.
- **F3** Legs are 75u long, start 13u either side of centre, and are straight thin lines. **No feet.**
- **F4** Arms start at the torso sides about 33u below the torso top. They are thin lines. **No hands.** (A held object simply touches the line end.)
- **F5** Outline is `#1E1F22` and uniform. Limb width is 1.5× the outline width. No sketchy or variable lines.
- **F6** Shading: light from the top-left, one flat shade shape per object. No gradients, highlights or texture (except Mr. Ledger's single head-shine mark).
- **F7** Face: no nose and no visible front ears. Eyes are small solid vertical ovals spaced about 0.3× the head width apart, at the head's vertical centre. Brows sit 17u above the eyes. The mouth sits 22u below the eyes.

**Fixed per character (identity keys)**

| Character | Never change |
|---|---|
| Marlow | Swoop tuft curling to his right · amber scarf with left-side tail · navy coat · red map-pin on the right lapel · thick bar brows |
| Rosa | High bun · teal hoodie with drawstrings |
| Vera | Grey blunt bob · round glasses · teal lanyard |
| Minister | Side-part hair · charcoal suit · lapel pin (the tie colour may change by country) |
| Ledger | Bald with shine · moustache · black suit · gold tie |
| Dev | Hi-vis orange vest with silver stripes (headwear may change by job) |
| Commons | Faceless · grey tints only (one red highlight allowed) |

**Allowed changes**
- **A1** Expressions: brows, eyes and mouth from the library only, plus the listed extras.
- **A2** Poses: limb lines, a body lean of up to 15°, and whole-body rotation for falling or lying only.
- **A3** Views: front, three-quarter, side or back, mirrored left or right. **When mirroring Marlow, mirror the whole figure, so the tuft and scarf tail swap sides together.** Never fix one and not the other.
- **A4** Props in hand: documents, boxes, phones, banknotes, briefcases, signs.
- **A5** Outer layers for weather or role: an umbrella, a winter hat *instead of* hair only for the Commons and Dev. **Marlow keeps his hair and scarf visible in every scene.**
- **A6** Scale in frame. Characters never get re-proportioned for close-ups; use camera crops instead.

**Rules of use**
- **R1** One expression at a time. No mixing (e.g. no happy eyes with an angry mouth unless it's in the library).
- **R2** In serious or tragic scenes, use only neutral, sad, serious or worried, with no extras. Prefer silhouettes or back views.
- **R3** Never change skin tones between videos.
- **R4** Never add realism (noses, fingers, detailed clothing folds) to "upgrade" a shot.
- **R5** Background detail must stay below character contrast. The characters are the cleanest, highest-contrast shapes in frame.
- **R6** Keep all character art in the `sheets/` vector files. Export new poses by editing `gen.py` or the SVGs, not by regenerating with AI.
- **R7** **Real people:** represent them as an archetype (usually the Minister) with a **name caption** and identifying context (flag, title). Don't caricature real faces or invent quotes. Commentary is fine; mockery of appearance is not.

---

## 9. Originality and brand checklist

- [x] An original cast. No hairstyle, outfit or colour combination is borrowed from the reference channel's characters.
- [x] Recognisable silhouettes for every character: tuft and scarf, bun, bob and glasses, side-part, bald and moustache, hard hat, faceless crowd.
- [x] One shared skeleton, so they belong to one universe.
- [x] Brand colours (amber, brick, teal) are shared between the characters and the data graphics.
- [x] Animation-friendly: limbs are single lines, there are no hands or feet to animate, and expressions are swappable layers.
- [ ] **Your next step:** run a quick originality search. Search YouTube and Google Images for "cartoon man amber scarf navy coat explainer" and similar, to make sure no existing channel already uses a near-identical mascot before you trademark or brand it.
