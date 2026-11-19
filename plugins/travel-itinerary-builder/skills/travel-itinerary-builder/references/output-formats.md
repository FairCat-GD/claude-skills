# Output formats

Two formats: **trip-themed PDF** (always produced — don't ask the user to choose) and **chat** (a fallback, only when the user explicitly asks for it or WeasyPrint can't run where you are). PDF is the only option that lives well on a phone, and that's where the user will actually read it during the trip.

---

## 1. Chat

Print the entire itinerary directly in the conversation as Markdown.

- Use H1 per day, H2 for parts of day, H3 per location block
- Map URLs as plain Markdown links
- Currency conversions inline
- Keep all six appendices, A–F (food, shopping, weather, things to watch out for, emergency contacts, city specialties), with the same letters and the same omissions as the PDF

---

## 2. PDF — trip-themed, mobile-friendly (default)

Build it as a properly designed document, not a dumped Word-to-PDF. This is what most travelers actually want.

### Approach

Build with HTML + CSS, render to PDF with **WeasyPrint**. The HTML/CSS approach lets you fully control typography, color, and spacing — that's what makes the difference between a beige report and a document the user is excited to open on the plane.

### Building the PDF — try in this order

1. **WeasyPrint is already there:** `python3 -c "import weasyprint"` succeeds. Use it.
2. **Install it in a virtual environment:** `python3 -m venv .venv && .venv/bin/pip install weasyprint`, or `uv run --with weasyprint python build.py`. Only in a disposable sandbox whose system Python refuses pip ("externally managed") is `pip install --break-system-packages weasyprint` acceptable — never on the user's own machine.
3. **WeasyPrint needs the Pango library from the system.** If importing it fails for want of Pango (`libgobject`, `libpango` in the error), Pango is missing or not found. Installing it changes the user's machine, so ask first: `brew install pango` on macOS, `apt install libpango-1.0-0 libpangoft2-1.0-0` on Debian or Ubuntu. On macOS with Homebrew, WeasyPrint finds it only with `DYLD_FALLBACK_LIBRARY_PATH="$(brew --prefix)/lib"` set when you run it.
4. **None of that is possible** (no code execution, no install allowed, the user declines): deliver in chat (section 1), and say in one line why there is no PDF and what would make one.

### Page setup

- **A4 portrait**, narrow margins: 12mm top/bottom, 14mm left/right
- Single column — designed to be read on a phone in portrait
- Fonts load from Google Fonts by `@import`, which needs the network. Offline the PDF still builds, silently, with the fallback fonts in each stack: Georgia or the system serif for headings, Helvetica, Arial or the system sans-serif for the body. The font check under *Rendering* tells you which you got.

### Theming — seasonal palette

The accent color is chosen by **season of travel**, not destination. This makes the same trip feel cooler in winter and warmer in summer, and keeps the cover printable without huge ink areas.

Derive season from the user's travel month (Northern Hemisphere by default — flip for Southern Hemisphere destinations like Bali, Sydney, Cape Town if dates clearly indicate a flipped season). A known month or season is enough to pick the accent — exact dates aren't required. Use the neutral palette only when no month or season is known at all.

| Season | Months (N. Hemi) | Mood | Accent | Accent Light | Accent Dark |
|---|---|---|---|---|---|
| Spring | Mar–May | soft mint | `#7ab089` | `#e8f3eb` | `#4f7e5d` |
| Summer | Jun–Aug | soft green | `#6f9a5f` | `#e4ede0` | `#4a6c3d` |
| Autumn | Sep–Nov | soft amber | `#c79150` | `#f5ebd9` | `#8e6432` |
| Winter | Dec–Feb | soft blue | `#7faac8` | `#e6eef6` | `#557a96` |
| No dates or season | — | neutral charcoal | `#5a5a5a` | `#ececec` | `#333333` |

**Why these colors:** muted and soft on purpose. They print acceptably and feel travel-appropriate without screaming. None is so dark that printing the cover or appendix headers exhausts an ink cartridge.

Use the accent sparingly:
- Title typography on the cover (color, not background)
- Subtle accent rules (thin lines, not bars)
- Day-header text accent (with thin rule, no full-bleed color)
- Hyperlink color
- Tip-line left border accent
- Snack-stop card border

Do not color body text. Do not fill more than ~10% of any given page with accent color. Reserve the saturated accent color for short strokes; let the page breathe in white.

### Typography

- **Headings:** "Playfair Display" for cover and appendix titles, "Inter" or "Source Sans" for body and inner headings.
- **Body:** ~10pt, line-height 1.5
- **Block labels** (bold): same family as body, 600 weight
- Avoid Comic Sans, Papyrus, or anything that screams 1998
- **No emoji or decorative glyphs in the PDF.** Emoji have no font in WeasyPrint and render as empty "tofu" boxes; symbol glyphs (arrows, stars, diamonds, etc.) are needless fragility. Use plain text only and let CSS do the visual work — tinted cards, thin rules, bold labels. So: snack stops are set apart by their card (no marker glyph), ratings read like "4.5/5 (Google Maps)", external links are plain hyperlinked words, and a note opens with a bold word ("Note —"). (Chat output may keep emoji — this is PDF-only.) After rendering, eyeball the pages for any stray boxes.

### Document structure

#### Cover page — printable, ink-light
**Do not use a full-bleed colored or gradient background.** Covers with large solid color fields cost users real money to print and we don't need that — typography does the work.

Layout (top to bottom on white):
- A thin accent rule (~80mm wide, 2–3pt) at the top, left-aligned
- Sub-label in small all-caps with the accent color: `TWO DAYS IN` / `A SOLO ITINERARY` / similar
- City name as the title — very large serif display type, **in the accent-dark color** (the typography is the visual hero)
- Dates underneath, in italic at body color
- Generous white space
- A small accent rule at the bottom, plus a one-line traveler-and-focus chip in muted color

The result: a confident, gallery-style title page that uses about 5% of the page area in color. Prints in minutes, costs cents.

#### Trip context page
- Single page summary as a definition list
- Small disclaimer about hours/fees verification

#### Day pages
- Day header — also ink-light: small "DAY N · [Date]" in accent caps, then the day title in accent-dark serif, with a thin accent rule beneath. **No full-bleed colored bar** (same printing-cost reason as the cover).
- Google Maps button styled as a pill link with accent border (outline, not fill) — "View today's route"
- Section headers (Morning/Lunch/Afternoon/Dinner) styled as serif italic with a thin underline
- Block design:
  - Number circle (accent-colored) + name as a sub-heading with a Wikipedia link (plain hyperlinked text)
  - Field labels in bold accent color, values in regular
  - "Tip" line indented with a left border in the accent color
  - **Lunch/dinner (meal) blocks on the route** sit on a tinted card (very light accent fill, rounded corners) to set them apart from the white sightseeing blocks — keep the number circle and the same fields, plus the Rating line
- **Snack/drink stop styling** — these are optional bonus stops between anchor blocks:
  - No number circle
  - Tinted background (very light accent), compact one-paragraph card
  - No marker glyph — the tinted background and indent set it apart; lead with the bold name
  - Italic body, ~9pt
  - Indented ~6mm from the left so they're visually distinct from main blocks
  - CSS: `.snack` in the skeleton below
- Avoid orphans — use `page-break-inside: avoid` on each block

#### Appendices
- Page break before each appendix that is present. Letters are fixed: one left out is skipped, and the rest keep theirs
- Numbered headers
- **Appendix A** (food picks): minimum 10, max 15 entries. Render as a styled table with on-route picks flagged via a colored pill. Include rating + source per row, and hyperlink each restaurant name to its official site (or the rating source if it has none). If the user declined food picks, the table spans every tier, labelled, and no pick carries the pill.
- **Appendix B** (shopping): name specific stores, flagships, brands — not generic categories.
- **Appendix C** (weather): only if dates or at least a season are known; omit the section entirely otherwise.
- **Appendix D** (safety): named scams, hotspots, cultural rules — no generic warnings.
- **Appendix E** (emergency): numbers, dialing notes, nearest 24h pharmacy/hospital.
- **Appendix F** (specialties & curiosities): 5–10 cards, each a tinted box with a serif heading and a 3–5 sentence guide-voice description — interesting facts/curiosities and signature foods & drinks to taste. Warm, lively, specific.

### Mobile readability checks

Before delivering, double-check:
- The page reads well on a laptop at fit-to-width and prints at full size. On a phone, the reader zooms into the single column: at full width a 6" phone shows A4's 10pt body at about 3pt. Keep everything in one column: then one zoom and vertical scrolling read the whole page, with no sideways panning.
- Links are clearly identifiable (color + underline).
- Page breaks fall at sensible places — never mid-block.

### Skeleton HTML/CSS

```html
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<style>
  /* @import must come first: CSS ignores an @import after any other rule */
  @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@700&family=Inter:wght@400;600&display=swap');
  @page { size: A4; margin: 12mm 14mm; }
  body { font-family: 'Inter', 'Helvetica Neue', Helvetica, Arial, sans-serif; font-size: 10pt; line-height: 1.5; color: #1a1a1a; }
  h1.cover-title { font-family: 'Playfair Display', Georgia, 'Times New Roman', serif; font-size: 64pt; color: var(--accent-dark); margin: 0; }
  .day-header { margin: 24px 0 16px; padding-bottom: 6px; border-bottom: 2px solid var(--accent); }
  .day-header .day-label { font-size: 9pt; letter-spacing: 0.12em; text-transform: uppercase; color: var(--accent); }
  .day-header .day-title { font-family: 'Playfair Display', Georgia, 'Times New Roman', serif; font-size: 20pt; color: var(--accent-dark); margin: 2px 0 0; }
  .block { page-break-inside: avoid; margin-bottom: 20px; }
  .block.meal { background: var(--accent-light); border-radius: 6px; padding: 8px 12px 5px; } /* on-route lunch/dinner */
  .label { font-weight: 600; }
  .tip { border-left: 3px solid var(--accent); padding-left: 10px; margin-top: 8px; }
  .snack { padding: 6px 10px; background: var(--accent-light); border-left: 2px solid var(--accent); margin: 0 0 4mm 8mm; font-size: 9pt; font-style: italic; }
  a { color: var(--accent); text-decoration: underline; }
  :root { --accent: #6f9a5f; --accent-light: #e4ede0; --accent-dark: #4a6c3d; } /* set per season — example: summer */
</style>
</head>
<body>
  <!-- cover, context, day pages, appendices A–F -->
</body>
</html>
```

### Rendering

```python
from weasyprint import HTML
HTML(string=html_content, base_url='.').write_pdf('Lisbon_4-day_itinerary.pdf')
```

Then check what you built (a text-only itinerary is small — typically well under 1 MB):

- **Page images,** to look at: `pdftoppm -png -r 80 -f 1 -l 4 Lisbon_4-day_itinerary.pdf page` where Poppler is installed; otherwise PyMuPDF, which installs with pip and needs nothing from the system (`pip install pymupdf`):

  ```python
  import fitz  # PyMuPDF
  doc = fitz.open('Lisbon_4-day_itinerary.pdf')
  for i in range(min(4, len(doc))):
      doc[i].get_pixmap(dpi=80).save(f'page-{i + 1}.png')
  print(sorted({f[3] for p in doc for f in p.get_fonts()}))  # the fonts embedded
  ```

- **Fonts:** `pdffonts Lisbon_4-day_itinerary.pdf`, or the last line above. Inter and Playfair Display mean the Google Fonts loaded; anything else is the fallback.

---

## Currency formatting

- Always show local first, home currency in parentheses with a tilde: `€12 (~$13)`
- Set the exchange rate once at the top of the document — small line in the Trip Context section: "Approx €1 ≈ $1.08 (rate at generation)"
- Don't update the rate per item; use one consistent number
- If local and home currency are the same, skip the conversion entirely

---

## Naming the output file

Use `<Destination>_<N>-day_itinerary.<ext>` — no spaces, no special characters. Examples:

- `Lisbon_4-day_itinerary.pdf`
- `Berlin_3-day_itinerary.pdf`

Save it and hand it over as `SKILL.md` says (Phase 5, *Save and hand it over*).
