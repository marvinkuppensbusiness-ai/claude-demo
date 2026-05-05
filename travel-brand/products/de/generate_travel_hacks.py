#!/usr/bin/env python3
"""Generate Apple-style Travel Hacks Guide PDF."""

from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm, cm
from reportlab.lib.colors import HexColor, white, black
from reportlab.pdfgen import canvas
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_JUSTIFY
from reportlab.platypus import Paragraph, Frame
from reportlab.lib.styles import ParagraphStyle
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
import os

# --- Colors ---
BLACK = HexColor("#1D1D1F")
DARK_GRAY = HexColor("#333333")
MID_GRAY = HexColor("#86868B")
LIGHT_GRAY = HexColor("#E5E5E7")
BG_GRAY = HexColor("#F5F5F7")
APPLE_BLUE = HexColor("#0071E3")
WHITE = HexColor("#FFFFFF")
SUBTITLE_GRAY = HexColor("#6E6E73")

# --- Page Setup ---
W, H = A4  # 595.27 x 841.89
MARGIN_L = 50
MARGIN_R = 50
MARGIN_T = 60
MARGIN_B = 60
CONTENT_W = W - MARGIN_L - MARGIN_R

# --- Try to register Helvetica Neue or fall back ---
def setup_fonts():
    font_paths = [
        "/System/Library/Fonts/HelveticaNeue.ttc",
        "/Library/Fonts/Helvetica Neue.ttf",
        "/System/Library/Fonts/Supplemental/Helvetica Neue.ttf",
    ]
    for fp in font_paths:
        if os.path.exists(fp):
            try:
                pdfmetrics.registerFont(TTFont("HN", fp, subfontIndex=0))
                pdfmetrics.registerFont(TTFont("HN-Bold", fp, subfontIndex=1))
                pdfmetrics.registerFont(TTFont("HN-Light", fp, subfontIndex=3))
                pdfmetrics.registerFont(TTFont("HN-Medium", fp, subfontIndex=6))
                return "HN", "HN-Bold", "HN-Light", "HN-Medium"
            except Exception:
                pass
    # Fallback
    return "Helvetica", "Helvetica-Bold", "Helvetica", "Helvetica-Bold"

FONT, FONT_BOLD, FONT_LIGHT, FONT_MEDIUM = setup_fonts()

OUTPUT = "/Users/marvinkuppens/Documents/Claude demo/travel-brand/products/de/travel-hacks-guide.pdf"


def draw_header(c, page_num, total_pages):
    """Minimal header + page number."""
    c.saveState()
    c.setFont(FONT_MEDIUM, 7)
    c.setFillColor(MID_GRAY)
    c.drawString(MARGIN_L, H - 35, "UNCLE MARV")
    # Page number bottom center
    c.setFont(FONT_LIGHT, 8)
    c.drawCentredString(W / 2, 30, f"{page_num} / {total_pages}")
    c.restoreState()


def draw_hairline(c, y, x1=None, x2=None):
    """Thin divider line."""
    c.saveState()
    c.setStrokeColor(LIGHT_GRAY)
    c.setLineWidth(0.5)
    c.line(x1 or MARGIN_L, y, x2 or (W - MARGIN_R), y)
    c.restoreState()


def draw_badge(c, text, x, y, color=APPLE_BLUE):
    """Draw a pill-shaped badge."""
    c.saveState()
    c.setFont(FONT_MEDIUM, 7)
    tw = c.stringWidth(text, FONT_MEDIUM, 7)
    pad_x = 8
    pad_y = 3
    badge_w = tw + pad_x * 2
    badge_h = 14
    # Background pill
    c.setFillColor(BG_GRAY)
    c.roundRect(x, y - 4, badge_w, badge_h, 7, fill=1, stroke=0)
    # Text
    c.setFillColor(color)
    c.drawString(x + pad_x, y, text)
    c.restoreState()
    return badge_w


def draw_hack(c, y, number, title, body, tag, tag_color=APPLE_BLUE):
    """Draw a single hack entry. Returns the new y position."""
    # Number
    c.saveState()
    c.setFont(FONT_BOLD, 9)
    c.setFillColor(MID_GRAY)
    num_str = f"#{number:02d}"
    c.drawString(MARGIN_L, y, num_str)

    # Badge
    badge_x = MARGIN_L + 35
    draw_badge(c, tag, badge_x, y, tag_color)

    c.restoreState()

    # Title
    y -= 20
    c.saveState()
    c.setFont(FONT_BOLD, 12)
    c.setFillColor(BLACK)
    c.drawString(MARGIN_L, y, title)
    c.restoreState()

    # Body text — use Paragraph for wrapping
    y -= 6
    style = ParagraphStyle(
        'hack_body',
        fontName=FONT_LIGHT,
        fontSize=9.5,
        leading=14,
        textColor=DARK_GRAY,
        alignment=TA_LEFT,
    )
    p = Paragraph(body, style)
    pw, ph = p.wrap(CONTENT_W, 200)
    y -= ph
    p.drawOn(c, MARGIN_L, y)

    y -= 18
    return y


def draw_quote(c, y, text):
    """Draw a centered quote with hairlines."""
    draw_hairline(c, y + 8)
    style = ParagraphStyle(
        'quote',
        fontName=FONT_LIGHT,
        fontSize=11,
        leading=16,
        textColor=MID_GRAY,
        alignment=TA_CENTER,
        spaceAfter=6,
    )
    # Use italic via markup
    p = Paragraph(f'<i>"{text}"</i>', style)
    pw, ph = p.wrap(CONTENT_W - 40, 200)
    y -= ph + 4
    p.drawOn(c, MARGIN_L + 20, y)
    y -= 12
    draw_hairline(c, y)
    return y - 20


def draw_chapter_header(c, y, chapter_num, title, subtitle):
    """Draw chapter title block with numbered circle."""
    # Apple-style numbered circle
    c.saveState()
    circle_r = 18
    circle_x = MARGIN_L + circle_r
    circle_y = y - 2
    c.setFillColor(APPLE_BLUE)
    c.circle(circle_x, circle_y, circle_r, fill=1, stroke=0)
    c.setFillColor(WHITE)
    c.setFont(FONT_BOLD, 16)
    num_str = f"{chapter_num:02d}"
    tw = c.stringWidth(num_str, FONT_BOLD, 16)
    c.drawString(circle_x - tw / 2, circle_y - 6, num_str)
    c.restoreState()

    # Title
    y -= 40
    c.saveState()
    c.setFont(FONT_BOLD, 30)
    c.setFillColor(BLACK)
    c.drawString(MARGIN_L, y, title)
    c.restoreState()

    # Subtitle
    y -= 22
    c.saveState()
    c.setFont(FONT_LIGHT, 12)
    c.setFillColor(SUBTITLE_GRAY)
    c.drawString(MARGIN_L, y, subtitle)
    c.restoreState()

    y -= 35
    draw_hairline(c, y)
    return y - 20


def draw_card(c, x, y, w, h, text_lines):
    """Draw a subtle card with rounded corners."""
    c.saveState()
    c.setFillColor(BG_GRAY)
    c.roundRect(x, y, w, h, 10, fill=1, stroke=0)
    c.restoreState()

    # Draw text inside card
    text_y = y + h - 22
    for i, (font, size, color, line) in enumerate(text_lines):
        c.saveState()
        c.setFont(font, size)
        c.setFillColor(color)
        c.drawString(x + 16, text_y, line)
        c.restoreState()
        text_y -= size + 4


# =====================================================
# PAGE BUILDERS
# =====================================================

def page_cover(c):
    """Page 1: Cover."""
    # Full background
    c.setFillColor(BLACK)
    c.rect(0, 0, W, H, fill=1, stroke=0)

    # Series tag
    y = H - 120
    c.setFont(FONT_MEDIUM, 9)
    c.setFillColor(MID_GRAY)
    c.drawCentredString(W / 2, y, "UNCLE MARV  --  TRAVEL GUIDE SERIES")

    # Main title
    y -= 60
    c.setFont(FONT_BOLD, 34)
    c.setFillColor(WHITE)
    # Multi-line title
    lines = ["Travel Hacks", "die wirklich", "funktionieren."]
    for line in lines:
        c.drawCentredString(W / 2, y, line)
        y -= 42

    # Subtitle
    y -= 15
    style = ParagraphStyle(
        'cover_sub',
        fontName=FONT_LIGHT,
        fontSize=11,
        leading=16,
        textColor=HexColor("#999999"),
        alignment=TA_CENTER,
    )
    p = Paragraph(
        "Und wie ich mit einer halben Couch, einem Klappstuhl<br/>und einer Prise Scham den Flughafen Weeze überlebt habe.",
        style
    )
    pw, ph = p.wrap(CONTENT_W - 40, 100)
    p.drawOn(c, MARGIN_L + 20, y - ph)
    y -= ph + 50

    # Stats bar
    c.setFont(FONT_BOLD, 14)
    c.setFillColor(WHITE)
    stats = "35+ HACKS   |   5 LÄNDER   |   1 COUCH ZU VIEL"
    c.drawCentredString(W / 2, y, stats)

    # Author info at bottom
    y = 110
    c.setFont(FONT_LIGHT, 10)
    c.setFillColor(MID_GRAY)
    c.drawCentredString(W / 2, y, "Von Marvin Kuppens")
    y -= 18
    c.setFont(FONT_LIGHT, 8)
    c.drawCentredString(W / 2, y, "marvinkuppens.business@gmail.com  ·  @ichheissemarrvin")

    c.showPage()


def page_intro(c):
    """Page 2: Einleitung + Inhaltsverzeichnis."""
    draw_header(c, 2, 12)

    y = H - MARGIN_T - 20

    # Title
    c.setFont(FONT_BOLD, 30)
    c.setFillColor(BLACK)
    c.drawString(MARGIN_L, y, "Meine Geschichte.")
    y -= 30

    # Body
    style = ParagraphStyle('intro', fontName=FONT_LIGHT, fontSize=10.5, leading=16,
                           textColor=DARK_GRAY, alignment=TA_LEFT)
    body1 = ("Ich bin Marvin. Ich fotografiere, filme, reise — und gelegentlich versuche ich, "
             "eine aufblasbare Couch mit in den Flieger zu schmuggeln. Über 23 Länder, "
             "verpasste Anschlüsse, Strände auf keiner Karte und jede Menge 3-Uhr-Nächte "
             "im Flughafen-Terminal. Jede dieser Erfahrungen hat mich etwas gelehrt.")
    p = Paragraph(body1, style)
    pw, ph = p.wrap(CONTENT_W, 200)
    y -= ph
    p.drawOn(c, MARGIN_L, y)

    # Quote
    y -= 20
    y = draw_quote(c, y,
        "Das Beste, was mir je passiert ist? Zu lernen, mit einem Rucksack auszukommen. "
        "Das Zweitbeste? Nicht nochmal eine Couch mitzunehmen.")

    # Body 2
    body2 = ("Diese Sammlung ist das Ergebnis echter Reisen — kein Bürowissen, keine kopierten Listen. "
             "Hier findest du Hacks, die ich selbst getestet habe. Manche sind offensichtlich, "
             "manche unerwartet. Alle machen einen Unterschied.")
    p = Paragraph(body2, style)
    pw, ph = p.wrap(CONTENT_W, 200)
    y -= ph
    p.drawOn(c, MARGIN_L, y)

    # Table of Contents
    y -= 45
    c.setFont(FONT_MEDIUM, 9)
    c.setFillColor(MID_GRAY)
    c.drawString(MARGIN_L, y, "WAS DICH ERWARTET")
    y -= 20

    draw_hairline(c, y + 8)
    y -= 8

    toc = [
        ("01", "Frühe Flüge & smarte Buchung"),
        ("02", "Handgepäck: Freiheit im Rucksack"),
        ("03", "Die 3-Gegenstände-Regel"),
        ("04", "Die Jacken-Strategie — legaler Schmuggel"),
        ("05", "Der richtige Rucksack"),
        ("06", "Packen wie ein Profi"),
        ("07", "Outdoor & Wandern"),
        ("08", "Gadgets die wirklich helfen"),
    ]

    for num, title in toc:
        c.setFont(FONT_BOLD, 11)
        c.setFillColor(APPLE_BLUE)
        c.drawString(MARGIN_L, y, num)
        c.setFont(FONT_LIGHT, 11)
        c.setFillColor(BLACK)
        c.drawString(MARGIN_L + 30, y, title)
        y -= 26

    # Footer line
    c.setFont(FONT_LIGHT, 7)
    c.setFillColor(MID_GRAY)
    c.drawString(MARGIN_L, MARGIN_B - 10, "© UncleMarv — marvinkuppens.business@gmail.com")

    c.showPage()


def page_chapter_01(c):
    """Kapitel 01: Frühe Flüge."""
    draw_header(c, 3, 12)
    y = H - MARGIN_T - 10

    y = draw_chapter_header(c, y, 1, "Frühe Flüge.", "Ja, 5 Uhr morgens. Nein, du wirst es nicht bereuen.")

    y = draw_hack(c, y, 1,
        "Früh fliegen = weniger Stress.",
        "Flüge vor 8 Uhr haben deutlich weniger Passagiere, kürzere Schlangen und — wenn du mit dem Auto fährst — fast keinen Verkehr auf dem Weg. An jedem Wochentag. Die Müdigkeit vergeht. Der Stress nicht.",
        "GameChanger")

    y = draw_hack(c, y, 2,
        "Sicherheitskontrolle am Morgen.",
        "Weniger Passagiere = weniger Wartezeit. Das bedeutet nicht, dass du fünf Minuten vor Boarding ankommen sollst — aber du wirst dich entspannter fühlen, wenn die Schlange drei Personen lang ist statt dreißig.",
        "Zeitersparnis")

    y = draw_hack(c, y, 3,
        "Skyscanner: Ziel auf 'Beliebig'.",
        "Flughafen eingeben (z.B. Köln, Düsseldorf, Dortmund), Zielort auf 'Überall', Datum auf 'Flexibel'. Dann nach Ländern filtern, die dich interessieren. So siehst du sofort welcher Monat am günstigsten ist.",
        "Sparer")

    y = draw_hack(c, y, 4,
        "Immer Reisepass mitnehmen.",
        "Auch innerhalb der EU, auch für 'nur drei Tage'. Der Reisepass hilft bei Ausweiskontrollen, Hotelbuchungen und — wenn du irgendwo ein Visum brauchst — rettet er buchstäblich deinen Trip.",
        "Pflicht")

    c.showPage()


def page_chapter_02(c):
    """Kapitel 02: Handgepäck."""
    draw_header(c, 4, 12)
    y = H - MARGIN_T - 10

    y = draw_chapter_header(c, y, 2, "Handgepäck.", "Aufgabegepäck kostet Geld, Zeit und deine Nerven.")

    # Intro text
    style = ParagraphStyle('ch_intro', fontName=FONT_LIGHT, fontSize=10, leading=15,
                           textColor=SUBTITLE_GRAY, alignment=TA_LEFT)
    intro = ("Wenn du einmal checkst, dass Aufgabegepäck bei Kurzflügen fast genauso viel kostet wie das Ticket "
             "selbst — und dass du am Zielort sowieso die Hälfte nie anziehst — ist der Schritt zu 'nur Handgepäck' "
             "keine Opferbereitschaft. Es ist Befreiung.")
    p = Paragraph(intro, style)
    pw, ph = p.wrap(CONTENT_W, 200)
    y -= ph
    p.drawOn(c, MARGIN_L, y)
    y -= 25

    y = draw_hack(c, y, 5,
        "Nur Handgepäck = direkt zur Sicherheit.",
        "Kein Check-in, kein Schlangestehen am Schalter, kein Warten am Band. Du landest und bist sofort draußen. Das spart im Schnitt 30–60 Minuten pro Trip — und 30–60 Euro obendrauf.",
        "Sparer")

    y = draw_hack(c, y, 6,
        "Maße kennen und einhalten.",
        "Jede Airline hat andere Maße für Handgepäck. Ryanair ist bekanntermaßen gnadenlos, Wizz Air misst am Gate. Kaufe einen Rucksack der exakt passt und miss ihn vorher nach.",
        "Achtung")

    y = draw_hack(c, y, 7,
        "Agadir Flughafen: Ernst genommen.",
        "Der Flughafen Agadir misst beim Rückflug buchstäblich jeden Millimeter. Steht ein Rad leicht über, wird es teuer. Das war 2024 so und wird sich wahrscheinlich nicht geändert haben. Du wurdest gewarnt.",
        "Airport-Tipp")

    y = draw_hack(c, y, 8,
        "Weeze: Die strikteste Kontrolle Deutschlands?",
        "Düsseldorf-Weeze kontrolliert schon in der Eingangshalle ob dein Gepäck passt. Alles muss in die Vorrichtung passen — kein Zentimeter darf herausschauen. Ich bin dort mit einer Couch und einem Klappstuhl angekommen. Ich bereue nichts. Außer der Couch. Und dem Klappstuhl.",
        "Echte Geschichte")

    c.showPage()


def page_chapter_03(c):
    """Kapitel 03: Die 3-Gegenstände-Regel."""
    draw_header(c, 5, 12)
    y = H - MARGIN_T - 10

    y = draw_chapter_header(c, y, 3, "Die 3-Gegenstände-Regel.", "Handy. Reisepass. Portemonnaie. Fertig.")

    # Three cards side by side
    card_w = (CONTENT_W - 20) / 3
    card_h = 70
    cards_data = [
        ("Handy", "Navigation, Ticket,", "Unterkunft — alles drauf"),
        ("Reisepass", "Identität, Visum,", "Hotelbuchung — nicht ohne"),
        ("Portemonnaie", "Karte, Bargeld,", "SIM-Kapazität — immer dabei"),
    ]

    for i, (title, line1, line2) in enumerate(cards_data):
        cx = MARGIN_L + i * (card_w + 10)
        # Card background
        c.saveState()
        c.setFillColor(BG_GRAY)
        c.roundRect(cx, y - card_h, card_w, card_h, 10, fill=1, stroke=0)
        # Card title
        c.setFont(FONT_BOLD, 11)
        c.setFillColor(BLACK)
        c.drawString(cx + 14, y - 22, title)
        # Card body
        c.setFont(FONT_LIGHT, 8.5)
        c.setFillColor(SUBTITLE_GRAY)
        c.drawString(cx + 14, y - 38, line1)
        c.drawString(cx + 14, y - 50, line2)
        c.restoreState()

    y -= card_h + 25

    # Body text
    style = ParagraphStyle('body3', fontName=FONT_LIGHT, fontSize=10, leading=15,
                           textColor=DARK_GRAY, alignment=TA_LEFT)
    body = ("Ich habe mir angewöhnt: bevor ich das Haus verlasse, fühle ich kurz nach — Handy, Reisepass, "
            "Portemonnaie. Sind diese drei Dinge dabei und ich bin angezogen, ist alles andere erst mal kein Problem. "
            "Grundsätzlich bekommst du alles Vergessene am Zielort: T-Shirts, Socken, Shampoo, Zahnbürste. "
            "Einen Reisepass nicht.")
    p = Paragraph(body, style)
    pw, ph = p.wrap(CONTENT_W, 200)
    y -= ph
    p.drawOn(c, MARGIN_L, y)

    y -= 20
    y = draw_quote(c, y,
        "Handy, Reisepass, Portemonnaie. Wenn ich diese drei Dinge habe und angezogen bin — dann bin ich bereit.")

    y = draw_hack(c, y, 9,
        "Visum & Einreisebestätigung: Sonderfall.",
        "Wer in Länder reist, die ein Visum oder eine digitale Einreisegenehmigung (z.B. ETIAS, ETA) erfordern, muss diese Dokumente zusätzlich parat haben. Das wird von der Regel nicht abgedeckt — das ist Hausaufgabe.",
        "Wichtig")

    c.showPage()


def page_chapter_04(c):
    """Kapitel 04: Die Jacken-Strategie."""
    draw_header(c, 6, 12)
    y = H - MARGIN_T - 10

    y = draw_chapter_header(c, y, 4, "Die Jacken-Strategie.", "Legaler Schmuggel seit 2019.")

    # Intro
    style = ParagraphStyle('ch_intro4', fontName=FONT_LIGHT, fontSize=10, leading=15,
                           textColor=SUBTITLE_GRAY, alignment=TA_LEFT)
    intro = ("Eine Jacke mit vielen Taschen ist kein Kleidungsstück. Es ist ein Tragevehikel. "
             "Seiten-, Hand-, Innentaschen — all das sind deine offiziellen Gepäckdepots für alles, "
             "was deinen Rucksack zu voll aussehen lässt. Beim Boarding: Jacke über den Arm. "
             "Kein Mitarbeiter schaut nach.")
    p = Paragraph(intro, style)
    pw, ph = p.wrap(CONTENT_W, 200)
    y -= ph
    p.drawOn(c, MARGIN_L, y)
    y -= 25

    y = draw_hack(c, y, 10,
        "Jacke mit vielen Taschen wählen.",
        "Seiten-, Hand-, Brust- und Innentaschen. Alles was in einen Zip-Beutel kommt (Flüssigkeiten, Ladekabel, Power Bank, Reisepass), kommt in die Jacke. Der Rucksack sieht dadurch deutlich weniger überfüllt aus.",
        "GameChanger")

    y = draw_hack(c, y, 11,
        "Boarding: Jacke über den Arm.",
        "Kurz vor dem Gate legst du die Jacke einfach über deinen Arm. Das ist keine Täuschung — du trägst die Jacke, sie ist Kleidung. So wird sie nicht als Gepäck gezählt. Ich hatte damit bisher keine einzige Diskussion.",
        "Bewährt")

    y = draw_hack(c, y, 12,
        "Vorderes Rucksackfach: nie überfüllen.",
        "Das vordere Fach ist das erste, das auffällt wenn der Rucksack aussieht als würde er gleich platzen. Alles was ins vordere Fach käme: ab in die Jacke.",
        "Optik-Hack")

    y = draw_hack(c, y, 13,
        "Zweite Jacke = doppeltes Volumen.",
        "Wer zwei Jacken mitnimmt (Sommer + Übergangs) trägt beim Boarding einfach beide — eine an, eine über dem Arm. Funktioniert. Wird nicht angesprochen. Keine weiteren Kommentare.",
        "Fortgeschritten")

    c.showPage()


def page_chapter_05(c):
    """Kapitel 05: Der Rucksack."""
    draw_header(c, 7, 12)
    y = H - MARGIN_T - 10

    y = draw_chapter_header(c, y, 5, "Der Rucksack.", "Nicht irgendein Rucksack. Der richtige.")

    y = draw_hack(c, y, 14,
        "Komprimierbarer Rucksack kaufen.",
        "Ein Rucksack, der sich von 25L auf 15L zusammenziehen lässt, ist Gold wert. Am Gate: klein. Tagsüber beim Erkunden: groß. Decathlon hat gute Optionen für 40–80 Euro.",
        "Top-Investition")

    y = draw_hack(c, y, 15,
        "Mini-Rucksack als Zweit-Lösung.",
        "Decathlon verkauft faltbare Rucksäcke in 5L, 10L und 15L — klein wie ein Tennisball, wenn zusammengefaltet. Passt in jede Jacken-Tasche oder in einen kleinen Rucksack-Schlitz. Für Tagesausflüge am Zielort unersetzlich.",
        "Decathlon")

    y = draw_hack(c, y, 16,
        "Schwere Schuhe: anziehen, nicht einpacken.",
        "Wanderschuhe, Winterboots, alles was Platz wegnimmt: beim Fliegen anziehen. Die leichteren Schuhe kommen in den Rucksack und du baust drumherum. Spart viel Volumen.",
        "Volumen-Trick")

    y = draw_hack(c, y, 17,
        "Socken & Unterwäsche in alle Ecken.",
        "Socken rollen und in Schuhe stopfen. Unterwäsche in jede freie Ecke im Rucksack. Das ist keine Kunst, aber fast jeder verschwendet diese Hohlräume mit Luft.",
        "Tetris-Prinzip")

    y -= 5
    y = draw_quote(c, y,
        "Gib Geld aus für einen guten Reiserucksack. Einmal die richtige Investition, kein jährliches Neudenken.")

    c.showPage()


def page_chapter_06(c):
    """Kapitel 06: Packen."""
    draw_header(c, 8, 12)
    y = H - MARGIN_T - 10

    y = draw_chapter_header(c, y, 6, "Packen.", "Weniger ist mehr. Aber Mütze ist Pflicht.")

    y = draw_hack(c, y, 18,
        "Erst mal Wochenendtrip machen.",
        "Bevor du für 3 Wochen packst: mach einen Wochenendtrip mit Handgepäck. Du wirst überrascht sein, wie wenig du wirklich brauchst. Das ist der schnellste Weg, deinen 'Ich brauche das alles'-Instinkt neu zu kalibrieren.",
        "Erstes Mal")

    y = draw_hack(c, y, 19,
        "Ein Basic-Outfit reicht meistens.",
        "Jeans + T-Shirt ist die universelle Lösung. Oder dein Lieblingsoutfit — das, in dem du dich am wohlsten fühlst. Das nimmst du und einen Wechsel. Mehr braucht es für 3–4 Tage selten.",
        "Minimalismus")

    y = draw_hack(c, y, 20,
        "Mütze immer einpacken.",
        "Frühling, Herbst — egal. Eine Mütze wiegt nichts, nimmt kaum Platz weg und rettet dich wenn es doch kälter wird als erwartet. Eine Cap geht auch, lässt sich sogar am Rucksack befestigen. Ich bevorzuge die Mütze. Du weißt jetzt warum.",
        "Unterschätzt")

    y = draw_hack(c, y, 21,
        "Shampoo & Kosmetik am Zielort kaufen.",
        "Außer du brauchst spezifische Produkte: alles Kosmetische kannst du vor Ort kaufen. Das spart Flüssigkeitsregeln-Stress, Gewicht und Volumen. Ein kleines Mitbringsel für die Heimreise.",
        "Sparer")

    y = draw_hack(c, y, 22,
        "Thermounterwäsche nicht vergessen.",
        "Klein, leicht, faltbar — und wenn du sie brauchst, gibt es nichts Besseres. Ob Herbstwanderung oder frische Hotelnacht: ein Set Thermounterwäsche nimmt kaum Platz weg und ist immer die richtige Entscheidung.",
        "Outdoor-Pflicht")

    c.showPage()


def page_chapter_07(c):
    """Kapitel 07: Outdoor & Wandern."""
    draw_header(c, 9, 12)
    y = H - MARGIN_T - 10

    y = draw_chapter_header(c, y, 7, "Outdoor & Wandern.", "Zehennägel schneiden. Ich meine es ernst.")

    y = draw_hack(c, y, 23,
        "Wanderschuhe anziehen — nicht einpacken.",
        "Wanderschuhe nehmen im Rucksack unverhältnismäßig viel Platz weg. Beim Flug anziehen, dann sind sie aus dem Weg. Dazu: ein kleines Paar Hausschuhe oder Sneakers für die Unterkunft.",
        "Volumen-Trick")

    y = draw_hack(c, y, 24,
        "Zehennägel VOR der Wanderung schneiden.",
        "Klingt banal. Ist es nicht. Bei langen Touren in engen Wanderschuhen kann ein zu langer Zehennagel innerhalb von 10 km zur Qual werden. Das wurde mir persönlich zum Verhängnis. Lern aus meinen Fehlern.",
        "Unterschätzt")

    y = draw_hack(c, y, 25,
        "Gaskocher von Decathlon (30–40 Euro).",
        "Klein, leicht, günstig. Der kleine Aufsatz-Gaskocher reicht für Tee, Suppe, Instantnudeln. Dazu: ein etwas größerer Becher dient gleichzeitig als Kochgefäß und als Staubox für Kleinteile.",
        "Decathlon")

    y = draw_hack(c, y, 26,
        "Hängematte + Moskitonetz statt Zelt.",
        "Wenn die Umgebung und das Wetter es erlauben: eine Hängematte mit integriertem Moskitonetz ist leichter, günstiger und ehrlich gesagt auch komfortabler als viele Zelte. Vor allem für Unruhschläfer mit Mückenallergie: absolutes Muss.",
        "Outdoor-Upgrade")

    y = draw_hack(c, y, 27,
        "Einmannzelt ohne Metallstäbe.",
        "Es gibt Zelte, die nur einen Ast oder einen Wanderstock brauchen um aufgestellt zu werden. Kein Metallgestänge, das in den Rucksack gestopft werden muss. Das Zelt spannt sich über den Stock in der Mitte. Kleiner, leichter, schneller aufgebaut.",
        "Gear-Tipp")

    c.showPage()


def page_chapter_08(c):
    """Kapitel 08: Gadgets."""
    draw_header(c, 10, 12)
    y = H - MARGIN_T - 10

    y = draw_chapter_header(c, y, 8, "Gadgets.", "Keine Gimmicks. Nur das was wirklich hilft.")

    y = draw_hack(c, y, 28,
        "Paracord — das universellste Gadget.",
        "Über 5 Länder in 2 Wochen war das Paracord von Anfang bis Ende dabei. Wäscheleine im Hotelzimmer. Gepäck komprimieren. Zelt spannen. Rucksack sichern. Du brauchst vielleicht 5–10 Meter und einen Karabiner. Das Ding kostet 5 Euro und ist unbezahlbar.",
        "#1 Gadget")

    y = draw_hack(c, y, 29,
        "Stirnlampe (Kopflampe).",
        "Nicht glamourös, aber praktisch. Beim Zelten, beim Suchen im dunklen Rucksack, beim spätnächtlichen Navigieren ohne Hände zu blockieren. Amazon oder jeder Outdoor-Shop. Klein, günstig.",
        "Outdoor-Basic")

    y = draw_hack(c, y, 30,
        "Kurbellampe (ohne Batterien).",
        "Eine kleine Taschenlampe, die man aufkurbeln kann — kein Akku, keine Batterien, kein 'leer wenn man sie braucht'. Gibt es für 5–8 Euro und funktioniert immer wenn alles andere schläft.",
        "Zero-Battery")

    y = draw_hack(c, y, 31,
        "Power Bank — keine Diskussion.",
        "Dein Handy ist dein Ticket, deine Navigation, dein Notruf. Ohne Akku bist du aufgeschmissen. Eine 10.000 mAh Power Bank reicht für 2–3 Ladungen, wiegt wenig und gehört in jeden Rucksack.",
        "Pflicht")

    y = draw_hack(c, y, 32,
        "Drohne einplanen: separat und unauffällig.",
        "Wer eine Drohne mitnimmt: eine separate Tasche dafür einplanen, am Gate nicht auffallen. Die Drohne + Akkus allein machen schon Gepäck sichtbar. Ich spreche aus Erfahrung. Weeze. Scham. Du weißt.",
        "Creator-Tipp")

    c.showPage()


def page_checklist(c):
    """Page 11: Checkliste."""
    draw_header(c, 11, 12)
    y = H - MARGIN_T - 10

    # Title
    c.setFont(FONT_BOLD, 30)
    c.setFillColor(BLACK)
    c.drawString(MARGIN_L, y, "Checkliste.")
    y -= 22

    c.setFont(FONT_LIGHT, 12)
    c.setFillColor(SUBTITLE_GRAY)
    c.drawString(MARGIN_L, y, "Alles auf einen Blick — vor dem nächsten Trip.")
    y -= 40

    draw_hairline(c, y)
    y -= 30

    # Two-column checklist
    items_left = [
        "Früher Flug gebucht?",
        "Nur Handgepäck?",
        "Handyakku 100%?",
        "Reisepass dabei?",
        "Portemonnaie dabei?",
        "Mütze eingepackt?",
        "Thermounterwäsche?",
        "Zehennägel geschnitten?",
    ]
    items_right = [
        "Power Bank eingepackt?",
        "Paracord dabei?",
        "Jacke mit Taschen?",
        "Rucksack-Maße ok?",
        "Mini-Rucksack dabei?",
        "Visum / ETA gültig?",
        "Stirnlampe / Kurbellampe?",
        "Skyscanner gecheckt?",
    ]

    col_w = CONTENT_W / 2
    row_h = 40

    for i in range(len(items_left)):
        for col, items in enumerate([items_left, items_right]):
            cx = MARGIN_L + col * col_w
            cy = y - i * row_h

            # Checkbox card
            c.saveState()
            c.setFillColor(BG_GRAY)
            c.roundRect(cx, cy - 10, col_w - 12, 32, 8, fill=1, stroke=0)

            # Checkbox square
            c.setStrokeColor(LIGHT_GRAY)
            c.setLineWidth(1.2)
            c.rect(cx + 12, cy - 2, 14, 14, fill=0, stroke=1)

            # Text
            c.setFont(FONT_LIGHT, 10)
            c.setFillColor(DARK_GRAY)
            c.drawString(cx + 34, cy, items[i])
            c.restoreState()

    y -= len(items_left) * row_h + 30

    # Bottom quote
    draw_hairline(c, y + 10)
    y -= 20
    c.setFont(FONT_BOLD, 13)
    c.setFillColor(BLACK)
    c.drawCentredString(W / 2, y, "Handy. Reisepass. Portemonnaie.")
    y -= 20
    c.setFont(FONT_LIGHT, 11)
    c.setFillColor(SUBTITLE_GRAY)
    c.drawCentredString(W / 2, y, "Der Rest findet sich.")

    c.showPage()


def page_closing(c):
    """Page 12: Abschluss."""
    # Light background
    c.setFillColor(BG_GRAY)
    c.rect(0, 0, W, H, fill=1, stroke=0)

    draw_header(c, 12, 12)

    # Centered content
    y = H / 2 + 120

    c.setFont(FONT_BOLD, 36)
    c.setFillColor(BLACK)
    c.drawCentredString(W / 2, y, "Gute Reise.")
    y -= 30
    c.setFont(FONT_LIGHT, 14)
    c.setFillColor(SUBTITLE_GRAY)
    c.drawCentredString(W / 2, y, "Und bitte kein Klappstuhl mehr.")

    y -= 60
    draw_hairline(c, y)
    y -= 30

    c.setFont(FONT_MEDIUM, 9)
    c.setFillColor(MID_GRAY)
    c.drawCentredString(W / 2, y, "MEHR HACKS, PRESETS & VIP-VORTEILE")

    y -= 30
    c.setFont(FONT_LIGHT, 11)
    c.setFillColor(DARK_GRAY)
    c.drawCentredString(W / 2, y, "marvinkuppens.business@gmail.com")
    y -= 18
    c.setFont(FONT_LIGHT, 10)
    c.setFillColor(MID_GRAY)
    c.drawCentredString(W / 2, y, "@ichheissemarrvin  ·  YouTube: Ichheissemarrvin")

    # Three product cards
    y -= 50
    card_w = (CONTENT_W - 30) / 3
    card_h = 50
    products = ["Travel Hacks PDF", "Cinematic Presets", "VIP Programm"]

    for i, prod in enumerate(products):
        cx = MARGIN_L + i * (card_w + 15)
        c.saveState()
        c.setFillColor(WHITE)
        c.roundRect(cx, y - 10, card_w, card_h, 10, fill=1, stroke=0)
        c.setFont(FONT_MEDIUM, 10)
        c.setFillColor(APPLE_BLUE)
        tw = c.stringWidth(prod, FONT_MEDIUM, 10)
        c.drawString(cx + (card_w - tw) / 2, y + 12, prod)
        c.restoreState()

    # Footer
    c.setFont(FONT_LIGHT, 7)
    c.setFillColor(MID_GRAY)
    c.drawCentredString(W / 2, 40, "© 2026 UncleMarv — Alle Rechte vorbehalten.")

    c.showPage()


def page_chapter_06_extra(c):
    """Extra page for Kapitel 06 overflow if needed — Packen continued."""
    pass


def page_chapter_08_page2(c):
    """Gadgets page 2 if needed."""
    pass


# =====================================================
# MAIN
# =====================================================

def build_pdf():
    c = canvas.Canvas(OUTPUT, pagesize=A4)
    c.setTitle("Travel Hacks die wirklich funktionieren — Uncle Marv")
    c.setAuthor("Marvin Kuppens")
    c.setSubject("Travel Hacks Guide")

    page_cover(c)        # 1
    page_intro(c)        # 2
    page_chapter_01(c)   # 3
    page_chapter_02(c)   # 4
    page_chapter_03(c)   # 5
    page_chapter_04(c)   # 6
    page_chapter_05(c)   # 7
    page_chapter_06(c)   # 8
    page_chapter_07(c)   # 9
    page_chapter_08(c)   # 10
    page_checklist(c)    # 11
    page_closing(c)      # 12

    c.save()
    print(f"PDF saved to: {OUTPUT}")
    print(f"Total pages: 12")


if __name__ == "__main__":
    build_pdf()
