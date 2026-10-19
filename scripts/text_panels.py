"""Animated terminal readouts for profile prose; plain-text content stays reusable."""
from html import escape
import textwrap
import xml.etree.ElementTree as ET

PANELS = {
    'intro': ('cat ~/profile/about.txt', [
        ('identity', 'Rifatur Rahman / Dhaka, Bangladesh'),
        ('education', 'BSc in Computer Science and Engineering student at American International University-Bangladesh (AIUB).'),
        ('focus', 'Building across the interface, API and database with C# and ASP.NET Core.'),
        ('seeking', 'Full Stack Developer Internship'),
    ]),
    'stockpilot': ('cat StockPilot/engineering.md', [
        ('scope', 'Inventory + sales: purchase receiving, POS, invoices, payments and stock movements. MVC and REST API share application services.'),
        ('inspect', 'SQL application locking, persisted retry keys, and role / ownership checks.'),
        ('tradeoff', 'Writes serialize for a small-business workload. No production deployment is claimed.'),
        ('stack', 'C# / ASP.NET Core MVC + Web API / EF Core / SQL Server / Bootstrap'),
    ]),
    'genergy': ('cat G-Energy/engineering.md', [
        ('scope', 'EV charging demo: Owner / Driver access, vehicle assignments, reservations, charging sessions and a demo wallet.'),
        ('inspect', 'Vehicle-specific charging permission, charging-to-wallet settlement and protected Admin operations.'),
        ('boundary', 'Charging, top-ups, payments and refunds are simulated. This is a development project.'),
        ('stack', 'React / TypeScript / ASP.NET Core Web API / EF Core / SQL Server'),
    ]),
    'incidentlens': ('cat IncidentLens/contribution.md', [
        ('my work', 'Dependency security, glob compatibility and CI reliability.'),
        ('inspect', 'Scoped compatibility adapter, regression fixtures, and bounds on nested / expanded patterns.'),
        ('context', 'The application uses Next.js, FastAPI, hybrid retrieval and LangGraph for evidence-based incident investigation.'),
        ('credit', 'Original application: Niloy Bhuiyan. Upstream history and MIT attribution preserved; I do not claim original authorship.'),
    ]),
    'stack': ('cat ~/profile/stack.txt', [
        ('interface', 'HTML / CSS / JavaScript / Bootstrap; React + TypeScript in G Energy'),
        ('application', 'C# / ASP.NET Core MVC / Web API'),
        ('data', 'Entity Framework Core / SQL Server'),
        ('verification', 'Unit, integration and browser checks / Git / GitHub Actions'),
        ('next', 'Contribute to full-stack features, learn through code review and deepen my .NET + relational data skills.'),
    ]),
}


def make_text(kind, narrow=False, animated=True):
    command, fields = PANELS[kind]
    width, font, char_limit, step = (600, 32, 26, 43) if narrow else (1200, 23, 77, 34)
    rows = []
    for label, value in fields:
        rows.append((f'[{label.upper()}]', '#71ffaf'))
        rows.extend((s, '#d9eee2') for s in textwrap.wrap(value, width=char_limit, break_long_words=False))
        rows.append(('', '#d9eee2'))
    rows.pop()
    height = 127+len(rows)*step+38
    p = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}" role="img" aria-labelledby="title desc">', f'<title id="title">{escape(command)}</title>', f'<desc id="desc">{escape(" ".join(f"{label}: {value}" for label,value in fields))}</desc>', '<style>@keyframes blink{0%,48%{opacity:1}49%,100%{opacity:0}}.cursor{animation:blink 1.6s step-end infinite}@media(prefers-reduced-motion:reduce){.motion{display:none}.cursor{animation:none}}</style>', f'<rect x="1" y="1" width="{width-2}" height="{height-2}" rx="9" fill="#050d0b" stroke="#214d38"/>']
    for i,c in enumerate(['#396048','#467b59','#71ffaf']):
        p.append(f'<circle cx="{22+i*17}" cy="23" r="4" fill="{c}"/>')
    def txt(x,y,s,size,color):
        return f'<text x="{x}" y="{y}" font-family="Consolas,Courier New,monospace" font-size="{size}" fill="{color}">{escape(s)}</text>'
    p.append(txt(91,29,'rifatur17@dev: ~/readout',16,'#9eb7ab'))
    p.append(f'<path d="M1 44H{width-1}" stroke="#214d38"/>')
    p.append(txt(28,92,'$ '+command,26 if narrow else 25,'#69e5ed'))
    for i,(s,color) in enumerate(rows):
        y=136+i*step
        if not s:
            continue
        p.append(txt(22,y,f'{i+1:02}',17,'#537363'))
        reveal_start=min(0.01+i*0.0015,0.05)
        reveal_end=reveal_start+0.08
        p.append(f'<defs><clipPath id="row-{i}"><rect x="70" y="{y-font-2}" width="{width-90}" height="{step}"><animate attributeName="width" values="0;0;{width-90};{width-90}" keyTimes="0;{reveal_start};{reveal_end};1" dur="24s" repeatCount="indefinite"/></rect></clipPath></defs>')
        p.append(f'<g clip-path="url(#row-{i})">'+txt(70,y,s,font,color)+'</g>')
    p.append(f'<path d="M22 {height-31}H{width-22}" stroke="#173e29"/>')
    p.append(txt(26,height-10,'// source-backed profile',16,'#658976'))
    p.append(f'<rect class="cursor" x="{width-51}" y="{height-21}" width="23" height="6" fill="#71ffaf"/>')
    p.append(f'<g class="motion"><circle r="3" fill="#69e5ed"><animateMotion path="M22 {height-31}H{width-22}" dur="5s" repeatCount="indefinite"/></circle></g>')
    p.append('</svg>')
    result='\n'.join(p)+'\n'
    if not animated:
        ET.register_namespace('', 'http://www.w3.org/2000/svg')
        tree=ET.fromstring(result)
        for parent in tree.iter():
            for child in list(parent):
                if child.tag.rsplit('}',1)[-1] in ('style','animate','animateMotion') or child.attrib.get('class')=='motion':
                    parent.remove(child)
        result=ET.tostring(tree,encoding='unicode')+'\n'
    return result
