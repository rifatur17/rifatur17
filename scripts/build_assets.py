"""Generate self-contained, GitHub-compatible SVGs. Python standard library only."""
from html import escape
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ASSETS = ROOT / "assets"


def make(theme, kind, narrow=False):
    dark = theme == "dark"
    bg, panel, ink, muted, line = ("#0d1117", "#151c27", "#f0f3f8", "#a5b2c5", "#303d50") if dark else ("#ffffff", "#f3f6fa", "#142036", "#526079", "#cbd5e3")
    green = "#d4f77d" if dark else "#476800"
    blue = "#8cb8ff" if dark else "#245bb5"
    coral = "#ffbb9d" if dark else "#a5411c"
    width = 720 if narrow else 1200
    height = (440 if kind == "header" else 430) if narrow else (412 if kind == "header" else 256)
    parts = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}" role="img" aria-labelledby="title desc">']
    titles = {"header": "Rifatur Rahman — Full Stack Developer", "stockpilot": "StockPilot — a shared write path", "genergy": "G Energy — one connected demo workflow", "incidentlens": "IncidentLens — maintenance with a defined boundary"}
    parts += [f'<title id="title">{titles[kind]}</title>', '<desc id="desc">Technical illustration. Full project descriptions and source links are available in the README.</desc>', f'<rect width="{width}" height="{height}" rx="18" fill="{bg}"/>']

    def text(x, y, s, size=18, color=ink, weight=400, mono=False, spacing=None):
        family = "Consolas, monospace" if mono else "Segoe UI, Arial, sans-serif"
        track = f' letter-spacing="{spacing}"' if spacing else ""
        parts.append(f'<text x="{x}" y="{y}" fill="{color}" font-family="{family}" font-size="{size}" font-weight="{weight}"{track}>{escape(s)}</text>')

    def rule(x1, y1, x2, y2, stroke=line):
        parts.append(f'<path d="M{x1} {y1}H{x2}" stroke="{stroke}"/>' if y1 == y2 else f'<path d="M{x1} {y1}L{x2} {y2}" stroke="{stroke}"/>')

    def box(x, y, w, h, stroke=line):
        parts.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="9" fill="{panel}" stroke="{stroke}"/>')

    def arrow(x, y, length=36, color=muted):
        parts.append(f'<path d="M{x} {y}h{length}m-6 -5 6 5-6 5" fill="none" stroke="{color}" stroke-width="2"/>')

    if kind == "header" and narrow:
        text(32, 44, "RR / ENGINEERING PORTFOLIO", 23, green, 600, True)
        rule(32, 65, 688, 65)
        text(32, 140, "Rifatur Rahman", 62, ink, 700)
        text(34, 185, "FULL STACK DEVELOPER", 27, muted, 600, True)
        text(32, 260, "From interface", 46, ink, 600)
        text(32, 315, "to integrity.", 46, green, 600)
        rule(32, 350, 688, 350)
        text(32, 399, "C# / ASP.NET CORE / SQL SERVER", 25, muted, 500, True)
    elif kind == "header":
        text(44, 48, "RR / ENGINEERING PORTFOLIO", 16, green, 600, True, "1.8")
        rule(44, 69, 1156, 69)
        text(44, 147, "Rifatur Rahman", 62, ink, 700)
        text(47, 187, "FULL STACK DEVELOPER", 19, muted, 600, True, "2")
        text(44, 257, "From interface", 40, ink, 600)
        text(44, 305, "to integrity.", 40, green, 600)
        text(46, 369, "C#  /  ASP.NET CORE  /  SQL SERVER", 17, muted, 500, True)
        # A vertical path, intentionally schematic rather than a performance dashboard.
        rule(757, 111, 757, 367)
        for y, n, title, detail, accent in [(116,"01","INTERFACE","MVC · React",blue),(204,"02","APPLICATION","Web API · shared services",green),(292,"03","DATA","EF Core · SQL Server",coral)]:
            box(789, y, 367, 70)
            text(811, y+27, n, 15, accent, 600, True)
            text(855, y+27, title, 16, accent, 600, True)
            text(855, y+53, detail, 17, muted)
            parts.append(f'<circle cx="757" cy="{y+35}" r="5" fill="{accent}"/>')
            rule(763,y+35,789,y+35)
    else:
        accent = {"stockpilot": green, "genergy": blue, "incidentlens": coral}[kind]
        meta = {"stockpilot": ("01 / STOCKPILOT", "SHARED WRITE PATH", [("MVC + REST API", "Same application services"), ("LedgerGate", "Serializable + app lock"), ("SQL Server", "Stock + ledger + retry key")], "DESIGN TRADEOFF", "Writes serialize for a small-business workload."), "genergy": ("02 / G ENERGY", "DEVELOPMENT DEMO", [("Reserve", "Owner / Driver access"), ("Charge", "Simulated session"), ("Settle", "Owner demo wallet")], "EXPLICIT BOUNDARY", "Charging and all money movements are simulated."), "incidentlens": ("03 / INCIDENTLENS", "MY MAINTENANCE FOCUS", [("Audit", "Dependency chain"), ("Adapt", "Glob compatibility"), ("Check", "Regression fixtures")], "ENGINEERING INTENT", "Preserve behavior. Bound expansion resources.")}[kind]
        if narrow:
            text(32, 43, meta[0], 26, accent, 600, True)
            for i, (title, detail) in enumerate(meta[2]):
                y = 76 + i * 114
                box(32, y, 656, 94)
                text(54, y+36, title, 32, ink, 600)
                text(54, y+72, detail, 28, muted)
                if i < 2:
                    parts.append(f'<path d="M360 {y+98}v12m-5 -5 5 5 5-5" fill="none" stroke="{accent}" stroke-width="2"/>')
            parts.append('</svg>')
            return "\n".join(parts) + "\n"
        text(32, 38, meta[0], 17, accent, 600, True, "1")
        text(755, 38, meta[1], 15, muted, 500, True, "1")
        rule(32, 57, 1168, 57)
        for i, (title, detail) in enumerate(meta[2]):
            x = 32 + i * 392
            box(x, 82, 352, 92)
            text(x+20, 116, title, 25, ink, 600)
            text(x+20, 146, detail, 18, muted)
            if i < 2:
                arrow(x+360, 128, 24, accent)
        text(32, 216, meta[3], 14, accent, 600, True, "1")
        text(276, 216, meta[4], 20, muted)
        parts.append(f'<rect x="32" y="238" width="1136" height="2" fill="{line}"/>')
    parts.append('</svg>')
    return "\n".join(parts) + "\n"


if __name__ == "__main__":
    ASSETS.mkdir(exist_ok=True)
    for theme in ("dark", "light"):
        for kind in ("header", "stockpilot", "genergy", "incidentlens"):
            (ASSETS / f"{kind}-{theme}.svg").write_text(make(theme, kind), encoding="utf-8")
            (ASSETS / f"{kind}-mobile-{theme}.svg").write_text(make(theme, kind, True), encoding="utf-8")
    print("Generated 16 self-contained SVG assets.")
