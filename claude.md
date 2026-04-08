# UncleMarv – Travel Brand & Digital Products

**Project Owner:** Marvin  
**Created:** April 2026  
**Status:** Pre-Launch (2-day sprint)

---

## 🎯 Mission & Vision

**What is UncleMarv?**  
A minimalist travel lifestyle brand selling digital products inspired by 23+ countries of travel. Products include wallpaper packs, cinematic LUTs, Lightroom presets, city map posters, and travel guides.

**Primary Goal (Next 6 Months):**  
Launch shop & generate first sales.

**Product Priority Ranking:**
1. **Travel Guides** (Content-Marketing-Hebel)
2. **Cinematic LUTs** (höchste Marge)
3. **Wallpaper Packs** (schnellster Launch)
4. **City Map Posters** (unique selling point)

---

## 🛠 Tech Stack

### Current Setup
- **Frontend:** Static HTML/CSS/JS (kein Framework)
- **Hosting:** GitHub Pages (`gh-pages` branch)
- **Payment:** Stripe Payment Links (Phase 1) → Stripe Elements (Phase 2)
- **Deployment:** Git push workflow via GitHub CLI

### Planned Evolution
- **Stay Static:** Maximale Performance, null Kosten
- **Phase 2:** Stripe Elements mit Vercel/Netlify Functions für bessere UX
- **Language Switch:** Deutsch/Englisch umschaltbar (beide Sprachen ab Launch)

---

## 🎨 Design System

### Color Palette
```css
--bg-primary: #0f0f0f;    /* Dark background */
--accent-gold: #c9a96e;   /* Gold accent */
--text-light: #ffffff;    /* Primary text */
--text-muted: #a0a0a0;    /* Secondary text */
```

### Typography (Apple-Inspired)
- **Font:** Inter (Google Fonts) oder SF Pro Display
- **Headers:** 
  - **Extra fett** (700-900 weight)
  - **Große Punktgrößen** (48px-72px für Hero)
  - Uppercase ODER Sentence Case (je nach Kontext)
  - Klare Hierarchie: H1 → H2 → H3 deutlich unterscheidbar
- **Body:** 
  - Regular/Medium weights (400-500)
  - Großzügiger Line-Height (1.6-1.8)
  - Nie kleiner als 16px

### Apple Design Philosophy
**KRITISCH:** Alle UncleMarv-Outputs (Website, PDFs, iBooks) folgen dem **Apple Lookalike Prinzip:**

✅ **Fette, dominante Titel**
- Headlines sind **Statement-Pieces**, nicht Afterthoughts
- Minimum 600 weight, besser 700-900
- Großzügiger Whitespace um Titel herum

✅ **Modern & Innovativ**
- Klare, geometrische Formen
- Subtile Schatten & Glows (sparsam!)
- Hochwertige Produkt-Fotografie
- Asymmetrische Layouts mit Bedacht

✅ **Konsistenz über alle Formate**
- **Website** = gleicher Vibe wie **PDFs** = gleicher Vibe wie **iBooks**
- Farben, Fonts, Spacing überall identisch
- Brand Recognition auf den ersten Blick

### Layout Principles
- **No clutter:** Viel Weißraum (bzw. dark space)
- **Grid-based:** Kompakte Produkt-Grids mit Before/After Previews
- **Mobile-first:** Responsive, touch-optimized
- **Inspiration:** Apple Produktseiten, Kinfolk Magazine, Arc Browser UI

### Spacing & Rhythm (NICHT VERHANDELBAR)
**Problem:** Texte übereinander, chaotische Abstände, Design-Fehler  
**Lösung:** Mathematisches Spacing-System

```css
/* 8px Base Unit System (wie Apple) */
--space-xs: 8px;
--space-sm: 16px;
--space-md: 24px;
--space-lg: 32px;
--space-xl: 48px;
--space-2xl: 64px;
--space-3xl: 96px;

/* Beispiel Anwendung */
section { padding: var(--space-2xl) 0; }
h1 { margin-bottom: var(--space-lg); }
p + p { margin-top: var(--space-md); }
```

**Regeln:**
- Nie random Pixel-Werte (z.B. 23px, 41px)
- Immer Vielfaches von 8px
- Zwischen Sections: Minimum 64px
- Um Headlines: Minimum 32px oben/unten

### Design Quality Checklist (Vor jeder Delivery)

**Layout:**
- [ ] Keine überlappenden Texte
- [ ] Keine abgeschnittenen Elemente
- [ ] Konsistente Abstände (8px-System)
- [ ] Grid-Alignment perfekt
- [ ] Responsive Breakpoints getestet (Mobile, Tablet, Desktop)

**Typography:**
- [ ] Titel sind **fett** (min. 600 weight)
- [ ] Klare Hierarchie (H1 > H2 > H3 erkennbar)
- [ ] Line-Height nie unter 1.4
- [ ] Keine zu langen Zeilen (max. 70 Zeichen)

**PDFs & iBooks spezifisch:**
- [ ] Seitenränder symmetrisch
- [ ] Headers/Footers konsistent
- [ ] Seitenzahlen nicht über Text
- [ ] Bilder nie pixelig (min. 150 DPI)
- [ ] Inhaltsverzeichnis funktioniert (iBooks)
- [ ] Links klickbar (PDFs)

**Farben:**
- [ ] Kontrast WCAG AA konform (min. 4.5:1)
- [ ] Gold-Akzent sparsam eingesetzt (Highlights only)
- [ ] Kein reines Schwarz auf Weiß (#0f0f0f besser)

### Design Don'ts
❌ Keine generischen Stock-Foto-Vibes  
❌ Keine überladenen Layouts  
❌ Keine kitschigen Travel-Klischees  
❌ Keine aufdringlichen CTAs  
❌ **NEU:** Keine dünnen, unleserlichen Fonts  
❌ **NEU:** Keine random Spacing-Werte  
❌ **NEU:** Keine chaotischen PDF-Layouts

---

## 💰 Produkte & Pricing

### Digitale Produkte
1. **Travel Guides** (PDF/Interactive)
   - Stadt-spezifische Insider-Tipps
   - Fokus: Content-Marketing & SEO
   
2. **Cinematic LUTs**
   - Für DaVinci Resolve, Premiere Pro, Final Cut
   - Höchste Gewinnmarge
   
3. **Wallpaper Packs**
   - Desktop & Mobile (4K/5K)
   - Schnellster Time-to-Market
   
4. **City Map Posters**
   - Minimalistisch, druckbar
   - Unique Selling Point

### VIP Loyalty Program
- **10-Tier System** (bereits entwickelt)
- Gold-basiertes Design
- Progressiver Unlock von Benefits

---

## 📝 Content & Copy

### Tonalität
**Selbstironisch & witzig** (wie Marvin's Kommunikationsstil)

Beispiele:
- ❌ "Explore the world with our curated guides"
- ✅ "Damit du nicht wieder vor verschlossenen Museen stehst"

- ❌ "Professional cinematic color grading"
- ✅ "Deine Clips sehen aus wie Netflix. Nur billiger."

### Copy-Workflow
- **Claude schreibt fertige Copy** (keine Drafts)
- Marvin gibt Feedback & finalisiert
- Headlines + Body zusammen, nicht getrennt

---

## 📱 Social Media Strategie

### Content-Kanäle (Launch Priority)
1. **Instagram** – Travel-Content von 23 Ländern
2. **TikTok** – Travel-Content von 23 Ländern
3. **Newsletter** – 2x pro Monat (nachhaltig)
4. **YouTube** – TBD (später)

### Content-Typen
- **Hauptfokus:** Travel-Content von den 23 Ländern
- Authentische Einblicke, keine Hochglanz-Influencer-Ästhetik
- Behind-the-Scenes der Produkt-Erstellung
- Mini-Guides & Reisetipps

### Newsletter-Strategie
- **Frequenz:** 2x pro Monat
- **Ziel:** Community-Building + Produkt-Launches
- **Stil:** Persönlich, self-aware, kein Marketing-Bla

---

## 💻 Arbeitsweise mit Claude

### Prompt-Stil
- **Token-effizient:** Kompakte Prompts bevorzugt (`/compact` in Claude Code)
- **File-Path-first:** Präzise Pfade statt lange Erklärungen
- **Variabel:** Unterschiedlich je nach Task-Komplexität

### Git Workflow
- **Branch:** `gh-pages` (production)
- **Commit Messages:** Deutsch
- **Tools:** GitHub CLI (`gh`), Homebrew
- **Deployment:** Push = Live (GitHub Pages auto-deploy)

### Claude Code Best Practices
1. `/compact` für schnelle Iterationen
2. Exakte File-Paths statt Suchen
3. Minimale Token-Usage für einfache Änderungen
4. Skill-basiertes Routing (docx, pptx, xlsx, pdf, frontend-design)

### File Creation Standards (KRITISCH)

**Jedes erstellte File (PDF, iBook, DOCX, HTML) MUSS folgende Kriterien erfüllen:**

#### 1. Fehlerfreiheit (Zero Tolerance)
- **Keine überlappenden Texte** – Bounding Boxes dürfen sich nicht überschneiden
- **Keine abgeschnittenen Elemente** – Alles muss im sichtbaren Bereich sein
- **Kein Content-Overflow** – Text passt in Container, kein Scrollen wo keins sein sollte
- **Keine Layout-Verschiebungen** – Elemente bleiben an festen Positionen

#### 2. Spacing-System (8px-Grid)
```
Sektion zu Sektion: 64px (--space-2xl)
Headline zu Content: 32px (--space-lg)
Absatz zu Absatz: 24px (--space-md)
Inline-Elemente: 16px (--space-sm)
Micro-Spacing: 8px (--space-xs)
```

**Bei PDFs zusätzlich:**
- Seitenränder: 48px rundherum
- Kopfzeile/Fußzeile: 32px vom Rand
- Zwischen Kapiteln: Neue Seite starten

#### 3. Typography-Hierarchie (Obligatorisch)
```
H1 (Hero): 48-72px, Weight 700-900, Margin-Bottom 32px
H2 (Section): 36-48px, Weight 700, Margin-Bottom 24px
H3 (Subsection): 24-32px, Weight 600, Margin-Bottom 16px
Body: 16-18px, Weight 400, Line-Height 1.6
Caption: 14px, Weight 400, Color muted
```

#### 4. Platzhalter-Management
**Wenn echte Inhalte fehlen:**
- Nutze **semantische** Platzhalter: "Dein Foto hier" statt "Image123.jpg"
- Kennzeichne klar mit `[PLATZHALTER]` Prefix
- Gib exakte Dimensionen an: "Bild: 1200x800px, Format: JPG/PNG"
- Zeige Aspect Ratio visuell (z.B. graue Box mit Maßen)

**Beispiel (PDF):**
```
┌─────────────────────────────┐
│  [PLATZHALTER: Hero Image]  │
│  1920x1080px (16:9)         │
│  Format: JPG, min. 150 DPI  │
└─────────────────────────────┘
```

#### 5. Qualitätssicherung vor Delivery
**Vor dem Absenden an Marvin:**
- [ ] File in Original-Software öffnen (PDF in Acrobat, DOCX in Word)
- [ ] Zoom auf 100%, 150%, 200% → alles lesbar?
- [ ] Alle Seiten durchblättern → Layout konsistent?
- [ ] Links/Navigation funktionieren?
- [ ] Fonts eingebettet? (PDFs)
- [ ] Bilder hochauflösend? (min. 150 DPI)

#### 6. Design-Fehler vermeiden

**Häufige Fehler & Lösungen:**

| Fehler | Ursache | Lösung |
|--------|---------|--------|
| Text überlappt Bild | Fehlende Margins | Padding 24px minimum |
| Titel abgeschnitten | Feste Container-Höhe | Min-height statt height |
| Inkonsistente Abstände | Manuelle Pixel-Werte | CSS Variables nutzen |
| Unscharfe Bilder | Falsche Auflösung | 2x Retina-Größe exportieren |
| PDF-Seitenumbruch mitten im Satz | Keine page-break Kontrolle | `page-break-inside: avoid` |

---

## 🚀 2-Tage-Launch-Plan

### Tag 1: Setup & Content
- [ ] Domain kaufen & DNS konfigurieren (`travelwithmarv.com` oder Alternative)
- [ ] Stripe Account → Payment Links für erste 3 Produkte erstellen
- [ ] Impressum & Datenschutz einbinden (bereits vorhanden)
- [ ] 3 Launch-Produkte vorbereiten (Downloads bereitstellen)
- [ ] Produktbeschreibungen schreiben (Claude)
- [ ] Social Media Accounts anlegen (Instagram, TikTok)

### Tag 2: Finalisierung & Go-Live
- [ ] Payment-Integration testen (Test-Käufe)
- [ ] Mobile Responsiveness prüfen
- [ ] Cross-Browser Testing (Chrome, Safari, Firefox)
- [ ] GitHub Pages Custom Domain verbinden
- [ ] HTTPS aktivieren
- [ ] Soft Launch: Website live schalten
- [ ] Ersten Newsletter-Draft vorbereiten

---

## 🔐 Rechtliches (Deutschland)

### DSGVO-Compliance
- Impressum vorhanden ✅
- Datenschutzerklärung vorhanden ✅
- Cookie-Consent (falls Tracking eingebaut wird)
- Stripe als Payment Processor (DSGVO-konform)

### Steuerliches
- Kleinunternehmerregelung prüfen (falls <22.000€ Umsatz/Jahr)
- Rechnungen mit deutscher USt-ID ausstellen
- Digitale Produkte = 19% MwSt. (Deutschland)

---

## 📦 File Structure (GitHub Repo)

```
/
├── index.html              # Landing Page
├── shop.html               # Produktübersicht
├── product-[name].html     # Einzelne Produktseiten
├── impressum.html
├── datenschutz.html
├── assets/
│   ├── css/
│   │   └── style.css       # Inline bevorzugt
│   ├── images/
│   │   ├── products/
│   │   └── hero/
│   └── downloads/          # Nicht public (Stripe Redirect)
└── CNAME                   # Custom Domain
```

---

## 🎯 Success Metrics (6 Monate)

- **Primary:** Erster Sale innerhalb 2 Wochen nach Launch
- **Secondary:** 100 Instagram Follower (organisch)
- **Tertiary:** 50 Newsletter-Subscriber
- **Stretch:** 10 Sales/Monat bis Ende Q2 2026

---

## 🧠 Wichtige Annahmen & Präferenzen

### Was Marvin mag
✅ Token-effiziente Kommunikation  
✅ Klare, direkte Anweisungen  
✅ Humor & Selbstironie  
✅ Apple-inspiriertes Design  
✅ Minimalistisch, nicht minimalistisch-langweilig  

### Was Marvin nicht mag
❌ Überkomplizierte Tech-Stacks  
❌ Generische AI-Ästhetik  
❌ Marketing-Buzzword-Bingo  
❌ Lange Erklärungen, wenn kurze reichen  

---

## 📚 Skills & Tools (Claude)

Wenn relevant, nutze diese Skills:
- **docx** – Word-Dokumente (Travel Guides)
- **pdf** – PDF-Erstellung (Produktdownloads)
- **pptx** – Präsentationen (falls B2B-Pitch)
- **xlsx** – Spreadsheets (Analytics, Produkt-Tracking)
- **frontend-design** – Website-Komponenten, UI-Design

---

## 🔄 Changelog

| Datum | Änderung |
|-------|----------|
| 2026-04-07 | claude.md erstellt – Pre-Launch Phase |

---

**Last Updated:** 2026-04-07  
**Next Review:** Nach Launch (ca. 2026-04-10)
