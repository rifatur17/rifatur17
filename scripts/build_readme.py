"""Build README image sources and an accessible, searchable prose transcript."""
from html import escape
from pathlib import Path
from text_panels import PANELS
import json

ROOT=Path(__file__).resolve().parents[1]


def scan_picture(kind):
    data=json.loads((ROOT/'data/github-public-snapshot.json').read_text())
    descriptions={'profile':'Rifatur Rahman / @rifatur17. Full Stack Developer. C# / ASP.NET Core / SQL Server. AIUB BSc CSE student in Dhaka, seeking a Full Stack Developer Internship. ASCII portrait derived from his actual public GitHub avatar.','activity':f'{data["calendar"]["totalContributions"]} actual GitHub contributions over 21 October 2025 to 20 October 2026. Desktop shows all 365 days; mobile shows the latest 13 weeks. The animated crawler is decorative and does not change counts.','signal':f'GitHub snapshot on 20 October 2026: {data["public_repositories"]} public repositories, {data["calendar"]["totalContributions"]} contributions, {len(data["primary_languages"])} primary repository languages. These are dated snapshot values.'}
    sources=[('(prefers-reduced-motion: reduce) and (max-width: 600px)',f'scan-still-{kind}-mobile.svg'),('(prefers-reduced-motion: reduce)',f'scan-still-{kind}.svg'),('(max-width: 600px)',f'scan-{kind}-mobile.svg')]
    return '<picture>\n'+''.join(f'  <source media="{media}" srcset="assets/{file}">\n' for media,file in sources)+f'  <img src="assets/scan-{kind}.svg" width="1200" alt="{escape(descriptions[kind],quote=True)}">\n</picture>'


def picture(kind, panel=False):
    if panel:
        alt=' '.join(label+': '+value for label,value in PANELS[kind][1])
        sources=[('(prefers-reduced-motion: reduce) and (max-width: 600px)',f'readout-still-{kind}-mobile.svg'),('(prefers-reduced-motion: reduce)',f'readout-still-{kind}.svg'),('(max-width: 600px)',f'readout-{kind}-mobile.svg')]
        fallback=f'readout-{kind}.svg'
    else:
        alt={'header':'Rifatur Rahman — animated full-stack developer terminal. C# / ASP.NET Core / SQL Server. Seeking a Full Stack Developer Internship.','stockpilot':'StockPilot: MVC and API share services; LedgerGate serializes stock and ledger writes through a SQL Server application lock.','genergy':'G Energy: reserve, charge and settle. Owner wallet and Driver access are distinct; charging and money movements are simulated.','incidentlens':'IncidentLens maintenance: audit dependencies, preserve glob compatibility and verify regression/resource bounds. Original application by Niloy Bhuiyan.'}[kind]
        sources=[('(prefers-reduced-motion: reduce) and (max-width: 600px)',f'still-{kind}-mobile.svg'),('(prefers-reduced-motion: reduce)',f'still-{kind}.svg'),('(max-width: 600px) and (prefers-color-scheme: dark)',f'motion-{kind}-mobile-dark.svg'),('(max-width: 600px)',f'motion-{kind}-mobile-light.svg'),('(prefers-color-scheme: dark)',f'motion-{kind}-dark.svg'),('(prefers-color-scheme: light)',f'motion-{kind}-light.svg')]
        fallback=f'motion-{kind}-light.svg'
    return '<picture>\n'+''.join(f'  <source media="{media}" srcset="assets/cyber-{file}">\n' for media,file in sources)+f'  <img src="assets/cyber-{fallback}" width="1200" alt="{escape(alt,quote=True)}">\n</picture>'


if __name__=='__main__':
    sections=[
        scan_picture('profile'),
        '[`[ portfolio ↗ ]`](https://rifatur17.github.io/) · [`[ CV ↓ ]`](https://rifatur17.github.io/assets/Rifatur_Rahman_CV.pdf) · [`[ email ]`](mailto:rifaturrahman1131@gmail.com) · [Text-only profile](docs/PROFILE_TEXT.md)',
        '## `profile.signal`',scan_picture('signal'),
        '## `contribution.activity`',scan_picture('activity'),
        '[`[ full contribution calendar ↗ ]`](https://github.com/rifatur17?tab=overview) · [`snapshot / 20 OCT 2026`](data/github-public-snapshot.json)',
        '## `ls ~/projects`',
    ]
    projects=[('01 / StockPilot','stockpilot','https://github.com/rifatur17/StockPilot-Inventory-Sales-Management','[`write gate source`](https://github.com/rifatur17/StockPilot-Inventory-Sales-Management/blob/main/src/StockPilot.Infrastructure/LedgerGate.cs) · [`application screenshot`](https://github.com/rifatur17/StockPilot-Inventory-Sales-Management/blob/main/docs/screenshots/dashboard-desktop.png) · [`test strategy`](https://github.com/rifatur17/StockPilot-Inventory-Sales-Management/blob/main/docs/TESTING.md)'),('02 / G Energy','genergy','https://github.com/rifatur17/G-Energy-Project-Demo','[`access rules`](https://github.com/rifatur17/G-Energy-Project-Demo/blob/main/backend/GEnergy.Api/Services/VehicleAccess.cs) · [`settlement source`](https://github.com/rifatur17/G-Energy-Project-Demo/blob/main/backend/GEnergy.Api/Services/Wallets/WalletChargingSettlement.cs) · [`verification record`](https://github.com/rifatur17/G-Energy-Project-Demo/blob/main/docs/member5-verification.md)'),('03 / IncidentLens','incidentlens','https://github.com/rifatur17/IncidentLens','[`adapter + regression tests`](https://github.com/rifatur17/IncidentLens/tree/main/tools/eslint-glob-compat) · [`my security change`](https://github.com/rifatur17/IncidentLens/commit/ab1025ba8f7e5c571396285971d433f95b228b13) · [`upstream / Niloy Bhuiyan`](https://github.com/Niloy-Bhuiyan/IncidentLens)')]
    for title,kind,repo,links in projects:
        sections.extend([f'### `{title}`',f'<a href="{repo}">\n{picture(kind)}\n</a>',picture(kind,True),f'[`[ repository ↗ ]`]({repo}) · {links}'])
    sections.extend(['## `cat ~/profile/stack.txt`',picture('stack',True),'### `connect --next`','[`rifaturrahman1131@gmail.com`](mailto:rifaturrahman1131@gmail.com) · [`portfolio / projects ↗`](https://rifatur17.github.io/projects/)'])
    (ROOT/'README.md').write_text('\n\n'.join(sections)+'\n',encoding='utf-8',newline='\n')
    text=['# Rifatur Rahman — profile text','Animation-free, searchable transcript of the terminal readouts.','Seeking a Full Stack Developer Internship.']
    for kind,(command,fields) in PANELS.items():
        text.extend([f'## {kind.title()}','\n\n'.join(f'**{label.title()}:** {value}' for label,value in fields)])
    text.append('[Portfolio](https://rifatur17.github.io/) · [CV](https://rifatur17.github.io/assets/Rifatur_Rahman_CV.pdf) · [Email](mailto:rifaturrahman1131@gmail.com)')
    snapshot=json.loads((ROOT/'data/github-public-snapshot.json').read_text())
    text.extend(['## GitHub activity snapshot / 20 October 2026',f'{snapshot["public_repositories"]} public repositories; {snapshot["calendar"]["totalContributions"]} contributions in the 365-day calendar; {len(snapshot["primary_languages"])} primary repository languages. The visible crawler is decorative; calendar tiles retain their actual daily counts.','[Source snapshot](../data/github-public-snapshot.json) · [Full calendar](https://github.com/rifatur17?tab=overview)'])
    (ROOT/'docs/PROFILE_TEXT.md').write_text('\n\n'.join(text)+'\n',encoding='utf-8',newline='\n')
    print('README and text-only transcript generated.')
