# Fraction AI — Landing Page Build Prompt

## Project Overview

Build a single-file `index.html` landing page for **Fraction AI** at `getfraction.ai`.

Fraction is an **AI automation agency** — not a SaaS product, not a chatbot company. They build AI agents and automation workflows for small businesses that can't afford a full AI engineering team. Think: fractional AI ops for businesses that need outcomes, not tools.

---

## Brand Voice

- Confident, direct, no hype
- Anti-buzzword ("we don't do magic, we do systems")
- Speaks to operators and business owners, not developers
- Tagline direction: **"The quiet machine behind your operations"** or **"Your fractional AI team"** — pick the strongest or write a better one that fits

---

## Visual Direction

**Dark / sleek** — think Vercel, Linear, Raycast.

- Background: near-black (e.g. `#080808` or `#0a0a0a`)
- Accent: pull directly from the logo palette — the **teal/mint** (`#00D4AA` approx) is the primary accent, with the **blue** (`#4A90E2` approx) as a secondary. Use mint as the dominant accent (CTA, glows, highlights), blue as a supporting tone.
- Typography: NOT Inter, NOT Space Grotesk. Use something distinctive. Consider pairing:
  - Display: something geometric or editorial (e.g. `DM Serif Display`, `Syne`, `Outfit`, `Cabinet Grotesk`)
  - Body: something clean and readable (e.g. `Geist`, `Figtree`, `Plus Jakarta Sans`)
  - Load from Google Fonts or Fontsource CDN
- Subtle noise/grain texture on background
- Very generous whitespace
- Minimal UI — no carousels, no complex nav, no modals

---

## Page Sections

### 1. Nav
- Logo: use `logo-dark.png` (the light/white variant — suited for dark backgrounds). Place it as an `<img>` tag. Assume the file is in the same directory as `index.html`. Height: ~32px, auto width.
- Right side: single link — "Get in touch" or scrolls to waitlist
- Sticky, minimal, subtle blur backdrop

### 2. Hero
- Large, commanding headline — use the brand voice above. Make it land.
- 2-line subheadline explaining the core value prop: small businesses get an AI team without hiring one
- Single CTA button → scrolls to waitlist
- Subtle animated background element (CSS only — e.g. slow-moving gradient orbs, a faint grid, or geometric lines breathing)

### 3. What We Do (3 pillars — brief, no fluff)
Use a horizontal card layout or asymmetric grid. Each card: icon (pure CSS or inline SVG), short title, 1–2 sentence description.

Pillars:
1. **AI Agents built for your role** — intake coordinators, reporting assistants, COO-level operators. Not generic chatbots.
2. **Automation that actually runs** — n8n-powered workflows connected to the tools you already use.
3. **Consulting that ships** — we design, implement, and maintain. You get outcomes, not access.

### 4. Waitlist / Early Access
- Section heading: something like "Work with us early" or "Get in before we're booked"
- 1–2 sentences of social proof framing (e.g. "We're selectively onboarding our first clients...")
- Email input + submit button
- Form: no backend needed — `mailto:` action or a placeholder `action="#"` with a JS success state
- On submit: show a thank-you message inline (JS, no page reload)

### 5. Footer
- "© 2025 Fraction AI"
- `getfraction.ai`
- Minimal — one line

---

## Assets

The following files will be in the same directory as `index.html`:

- `logo-dark.png` — light/white variant of the Fraction AI logo. Use this in the nav and footer on the dark background.
- `logo.png` — dark text variant. Do not use on the dark page; keep as a reference for brand colors only.

**Brand colors extracted from logo:**
- Mint/teal: `#00D4AA`
- Blue: `#4D8EFF`
- Warm grey/taupe: `#7A7060`

---



- **Single file**: everything in `index.html` — CSS in `<style>`, JS in `<script>`
- No frameworks, no build step — pure HTML/CSS/JS
- Fonts loaded from Google Fonts CDN
- Fully responsive (mobile-first)
- Smooth scroll behavior
- No external JS dependencies (no jQuery, no libraries)
- All animations CSS-only unless trivial JS is needed for the form
- Self-hostable via Docker (nginx static server)

---

## Aesthetic Details to Nail

- Grain/noise overlay on the background (CSS SVG filter or a subtle `background-image` trick)
- The accent color should appear: on the CTA button, on section dividers or subtle borders, and as a glow/halo on the hero element
- Cards should use glass-morphism or very subtle border (`1px solid rgba(255,255,255,0.07)`) with a slight background lift
- Micro-animations: fade-in on scroll (use `IntersectionObserver`), button hover scale/glow
- The overall feeling should be: **premium ops tooling, not startup fluff**

---

## Deliverable

Single file: `index.html`

Ready to drop into an nginx Docker container with zero dependencies.
