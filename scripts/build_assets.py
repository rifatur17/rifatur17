"""Build original terminal-style profile art; no runtime services or dependencies."""
from html import escape
from pathlib import Path
import xml.etree.ElementTree as ET
from text_panels import PANELS, make_text

ROOT = Path(__file__).resolve().parents[1]
ASSETS = ROOT / "assets"


def make(theme, kind, narrow=False, animated=True):
    # The terminal stays dark in either GitHub theme, like an embedded code window.
    bg, panel, ink = "#050d0b", "#091812", "#e5fff0"
    green, cyan, muted, line = "#71ffaf", "#69e5ed", "#9eb7ab", "#214d38"
    width = 720 if narrow else 1200
    height = (570 if narrow else 500) if kind == "header" else (460 if narrow else 310)
    title = {"header": "Rifatur Rahman — full-stack engineering terminal", "stockpilot": "StockPilot — inventory write path", "genergy": "G Energy — charging and wallet boundaries", "incidentlens": "IncidentLens — dependency security maintenance"}[kind]
    p = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}" role="img" aria-labelledby="title desc">', f'<title id="title">{escape(title)}</title>', '<desc id="desc">Animated conceptual engineering schematic, not live telemetry. Project details and source links follow in the README.</desc>', '<defs><pattern id="grid" width="28" height="28" patternUnits="userSpaceOnUse"><path d="M28 0H0V28" fill="none" stroke="#123323" stroke-width="0.6"/></pattern><radialGradient id="glow"><stop stop-color="#14663e" stop-opacity="0.32"/><stop offset="1" stop-color="#050d0b" stop-opacity="0"/></radialGradient></defs>', f'<rect x="1" y="1" width="{width-2}" height="{height-2}" rx="12" fill="{bg}" stroke="{line}"/>', f'<rect x="2" y="44" width="{width-4}" height="{height-46}" fill="url(#grid)"/>', f'<ellipse cx="{width-180}" cy="{height//2}" rx="360" ry="260" fill="url(#glow)"/>']

    p.append('<style>@keyframes blink{0%,48%{opacity:1}49%,100%{opacity:0}}.cursor{animation:blink 1.6s step-end infinite}@media(prefers-reduced-motion:reduce){.motion{display:none}.cursor{animation:none;opacity:1}}</style>')

    def text(x, y, s, size=18, color=ink, weight=400, spacing=None):
        track = f' letter-spacing="{spacing}"' if spacing else ""
        p.append(f'<text x="{x}" y="{y}" fill="{color}" font-family="Consolas, Courier New, monospace" font-size="{size}" font-weight="{weight}"{track}>{escape(s)}</text>')

    def path(d, stroke=line, sw=1):
        p.append(f'<path d="{d}" fill="none" stroke="{stroke}" stroke-width="{sw}"/>')

    def box(x, y, w, h, stroke=line):
        p.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="4" fill="{panel}" stroke="{stroke}"/>')

    def dot(x, y, color=green, r=3):
        p.append(f'<circle cx="{x}" cy="{y}" r="{r}" fill="{color}"/>')

    def arrow(x, y, length=24, color=green):
        path(f'M{x} {y}h{length}m-6 -5 6 5-6 5', color, 2)

    def packet(d, seconds=4, delay=0, color=green, radius=4):
        # Native SVG motion works inside GitHub image elements; no script runs.
        p.append(f'<g class="motion"><circle r="{radius+5}" fill="{color}" opacity="0.1"><animateMotion path="{d}" dur="{seconds}s" begin="{delay}s" repeatCount="indefinite"/></circle><circle r="{radius}" fill="{color}"><animateMotion path="{d}" dur="{seconds}s" begin="{delay}s" repeatCount="indefinite"/></circle></g>')

    # A slow scanner travels across the grid. It is an illustration, not live telemetry.
    p.append(f'<g class="motion" opacity="0.16"><rect x="2" y="44" width="{width-4}" height="2" fill="{green}"/><rect x="2" y="36" width="{width-4}" height="8" fill="{green}" opacity="0.15"/><animateTransform attributeName="transform" type="translate" from="0 0" to="0 {height-48}" dur="8s" repeatCount="indefinite"/></g>')

    if kind == "header":
        # Discrete code streams sit in negative space, behind the stable identity text.
        for i, xx in enumerate(([567, 631, 681] if narrow else [531, 581, 1118])):
            p.append(f'<g class="motion" opacity="0.17" fill="{green}" font-family="Consolas,monospace" font-size="13"><text x="{xx}" y="-30">01</text><text x="{xx}" y="-8" opacity="0.6">10</text><text x="{xx}" y="14" opacity="0.3">01</text><animateTransform attributeName="transform" type="translate" from="0 -40" to="0 {height+40}" dur="{7+i*2}s" begin="{-i*2}s" repeatCount="indefinite"/></g>')

    for i, color in enumerate(["#396048", "#467b59", green]):
        dot(22+i*17, 23, color, 4)
    chrome = "rifatur17@dev: ~" if kind == "header" else f'~/projects/{kind} — source map'
    text(91, 29, chrome, 16, muted)
    text(width-95, 29, "UTF-8", 14, muted)
    path(f'M1 44H{width-1}')

    if kind == "header":
        x, y = (32, 98) if narrow else (42, 102)
        text(x, y, "$ whoami", 25 if narrow else 22, green)
        for index, yy in enumerate((y+82,y+165)):
            p.append(f'<defs><clipPath id="name-{index}"><rect x="{x-3}" y="{yy-90}" width="600" height="100"><animate attributeName="width" values="0;0;600;600" keyTimes="0;{0.02+index*0.06};{0.1+index*0.06};1" dur="24s" repeatCount="indefinite"/></rect></clipPath></defs>')
        p.append('<g clip-path="url(#name-0)">')
        text(x-2, y+82, "RIFATUR", 76 if narrow else 82, ink, 700, "1")
        p.append('</g><g clip-path="url(#name-1)">')
        text(x-2, y+165, "RAHMAN", 76 if narrow else 82, green, 700, "1")
        p.append('</g>')
        p.append(f'<rect class="cursor" x="{x+(286 if narrow else 308)}" y="{y+173}" width="43" height="8" fill="{green}"/>')
        text(x, y+210, "FULL STACK DEVELOPER", 27 if narrow else 24, cyan, 700)
        text(x, y+260, "C#  /  ASP.NET CORE  /  SQL SERVER", 25 if narrow else 19, muted)
        if narrow:
            path('M32 389H688')
            text(32, 433, "> UI → API → DATABASE", 28, green)
            text(32, 479, "AIUB / CSE STUDENT", 24, muted)
            text(32, 527, "SEEKING: FULL-STACK INTERNSHIP", 23, cyan)
            path('M32 549H688', line)
            packet('M32 549H688', 5, 0, cyan)
        else:
            box(713, 83, 447, 308)
            text(734, 114, "application.topology", 16, green)
            text(734, 141, "// conceptual request path", 14, muted)
            path('M734 157H1138')
            for yy, label, detail, accent in [(178,"UI","MVC / React",green),(246,"API","ASP.NET Core",cyan),(314,"DATA","EF Core / SQL",green)]:
                box(744, yy, 78, 42, accent)
                text(759, yy+28, label, 17, accent, 700)
                arrow(834, yy+21, 32, accent)
                text(882, yy+28, detail, 18, ink)
                if yy < 314:
                    path(f'M783 {yy+42}v26', line, 2)
            path('M42 414H1158')
            text(42, 455, "[ AIUB / CSE ]", 18, muted)
            text(325, 455, "seeking: full-stack internship", 19, cyan)
            text(1020, 455, "</> RR", 19, green, 700)
            packet('M783 220V246', 2.8, 0, green)
            packet('M783 288V314', 2.8, -1.4, cyan)
            for yy in (199, 267, 335):
                packet(f'M834 {yy}H866', 2.4, -yy/100, cyan, 3)
            # Rotating reticle bridges identity and architecture in the free center column.
            dot(637, 248, green, 5)
            for radius, dur, reverse in [(37,14,False),(49,22,True)]:
                p.append(f'<g class="motion"><circle cx="637" cy="248" r="{radius}" fill="none" stroke="{green}" stroke-opacity="0.5" stroke-dasharray="12 9 2 9"/><circle cx="{637+radius}" cy="248" r="3" fill="{cyan}"/><animateTransform attributeName="transform" type="rotate" from="0 637 248" to="{-360 if reverse else 360} 637 248" dur="{dur}s" repeatCount="indefinite"/></g>')
            text(607, 321, "</>", 24, green)
    elif kind == "stockpilot":
        if narrow:
            text(28, 92, "$ trace stock.write", 29, green, 700)
            rows = [("01", "MVC + REST API", "shared services"), ("02", "LedgerGate", "serializable + SQL app lock"), ("03", "SQL Server", "stock + ledger + retry keys")]
            for i, (n, label, detail) in enumerate(rows):
                y = 119+i*99
                box(28, y, 664, 82)
                text(45, y+34, n, 24, green)
                text(103, y+34, label, 29, ink, 700)
                text(103, y+65, detail, 25, muted)
            text(28, 444, "// deliberate write serialization", 24, cyan)
            packet('M28 119V399', 4, 0, green)
        else:
            text(28, 83, "$ trace stock.write", 22, green, 700)
            text(28, 113, "INVENTORY CONSISTENCY / IMPLEMENTATION MAP", 15, muted)
            box(28, 138, 528, 135)
            for y, n, s, col in [(170,"01","begin serializable transaction",ink),(202,"02","acquire SQL application lock",green),(234,"03","write stock + ledger; commit",ink)]:
                text(45,y,n,16,muted)
                text(88,y,s,19,col)
            text(599, 154, "MVC + API", 21, cyan, 700)
            arrow(750,148,40)
            text(814,154,"shared services",20,ink)
            path('M939 170V196H682V219',green,2)
            box(600,219,155,49,green)
            text(617,250,"LedgerGate",19,green)
            arrow(770,244,39)
            box(824,219,346,49)
            text(841,250,"SQL / persisted retry keys",18,ink)
            text(600,293,"// small-business write workload",16,muted)
            packet('M750 148H790', 2.8, 0, cyan)
            packet('M939 170V196H682V219', 4, -1, green)
            packet('M770 244H809', 2.8, -1.4, cyan)
            p.append(f'<rect class="motion" x="29" y="139" width="3" height="30" fill="{green}"><animateTransform attributeName="transform" type="translate" values="0 0;0 0;0 32;0 32;0 64;0 64;0 0" dur="6s" repeatCount="indefinite"/></rect>')
    elif kind == "genergy":
        if narrow:
            text(28, 92, "$ trace charging.flow", 29, green, 700)
            for i,(name,detail) in enumerate([("RESERVE","Owner / Driver access"),("CHARGE","simulated charging session"),("SETTLE","Owner demo wallet")]):
                y=119+i*99
                box(28,y,664,82)
                text(48,y+34,name,29,cyan,700)
                text(48,y+65,detail,25,muted)
            text(28,444,"// charging + money are simulated",24,green)
            packet('M28 119V399', 4, 0, cyan)
        else:
            text(28,83,"$ trace charging.flow",22,green,700)
            text(780,83,"[ DEVELOPMENT DEMO ]",18,cyan)
            for i,(name,detail) in enumerate([("01 / RESERVE","Owner / Driver access"),("02 / CHARGE","simulated session"),("03 / SETTLE","Owner demo wallet")]):
                x=28+i*392
                box(x,113,352,107)
                text(x+19,151,name,23,cyan,700)
                text(x+19,191,detail,19,ink)
                if i<2:
                    arrow(x+358,165,28)
            path('M28 245H1170')
            text(28,281,"// charging + top-ups + payments + refunds are simulated",19,green)
            packet('M386 165H414', 2.5, 0, green)
            packet('M778 165H806', 2.5, -1.25, cyan)
            p.append(f'<rect class="motion" x="439" y="212" width="2" height="3" fill="{green}"><animate attributeName="width" values="2;294;294;2" keyTimes="0;0.7;0.9;1" dur="7s" repeatCount="indefinite"/></rect>')
    else:
        if narrow:
            text(28,92,"$ inspect maintenance.scope",27,green,700)
            for i,(label,detail) in enumerate([("AUDIT","dependency chain"),("ADAPT","glob compatibility boundary"),("VERIFY","regression + resource bounds")]):
                y=119+i*99
                box(28,y,664,82)
                text(48,y+34,label,29,cyan,700)
                text(48,y+65,detail,25,muted)
            text(28,444,"// upstream authorship preserved",24,green)
            packet('M28 119V399', 4, 0, green)
        else:
            text(28,83,"$ inspect maintenance.scope",22,green,700)
            text(28,113,"DEPENDENCY SECURITY / COMPATIBILITY / CI",15,muted)
            box(28,137,528,137)
            text(49,169,"Next ESLint",21,cyan,700)
            text(49,202,"└─ fast-glob",20,ink)
            text(49,237,"   └─ scoped compatibility adapter",19,green)
            text(600,160,"[01] preserve glob behavior",21,ink)
            text(600,199,"[02] bound expansion resources",21,green)
            text(600,238,"[03] check regression fixtures",21,ink)
            text(28,297,"// original app: Niloy Bhuiyan / my focus: security + maintenance",17,muted)
            packet('M49 180V231H79', 4.5, 0, cyan, 3)
            p.append(f'<rect class="motion" x="586" y="144" width="3" height="21" fill="{green}"><animateTransform attributeName="transform" type="translate" values="0 0;0 0;0 39;0 39;0 78;0 78;0 0" dur="6s" repeatCount="indefinite"/></rect>')
    p.append('</svg>')
    result = "\n".join(p)+"\n"
    if not animated:
        ET.register_namespace('', 'http://www.w3.org/2000/svg')
        tree = ET.fromstring(result)
        for parent in tree.iter():
            for child in list(parent):
                if child.tag.rsplit('}',1)[-1] in ('style','animate','animateMotion','animateTransform') or child.attrib.get('class') == 'motion':
                    parent.remove(child)
        result = ET.tostring(tree, encoding='unicode')+'\n'
        result = result.replace('Animated conceptual', 'Animation-free conceptual')
    return result


if __name__ == "__main__":
    ASSETS.mkdir(exist_ok=True)
    for theme in ("dark", "light"):
        for kind in ("header", "stockpilot", "genergy", "incidentlens"):
            for narrow in (False, True):
                name = f"motion-{kind}{'-mobile' if narrow else ''}-{theme}.svg"
                (ASSETS/name).write_text(make(theme,kind,narrow),encoding="utf-8",newline="\n")
    for kind in ("header", "stockpilot", "genergy", "incidentlens"):
        for narrow in (False, True):
            name = f"still-{kind}{'-mobile' if narrow else ''}.svg"
            (ASSETS/name).write_text(make('dark',kind,narrow,False),encoding="utf-8",newline="\n")
    for kind in PANELS:
        for narrow in (False, True):
            for animated in (False, True):
                name=f"readout-{'still-' if not animated else ''}{kind}{'-mobile' if narrow else ''}.svg"
                (ASSETS/name).write_text(make_text(kind,narrow,animated),encoding='utf-8',newline='\n')
    print("Generated 44 terminal SVG assets, including animated prose and static alternatives.")
