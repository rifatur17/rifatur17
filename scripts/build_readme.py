"""CV-aligned profile with readable native Markdown and one original banner."""
from pathlib import Path
import json

ROOT=Path(__file__).resolve().parents[1]


def picture(kind,alt):
    sources=[('(prefers-reduced-motion: reduce) and (max-width: 600px)',f'reference-still-{kind}-mobile.svg'),('(prefers-reduced-motion: reduce)',f'reference-still-{kind}.svg'),('(max-width: 600px)',f'reference-{kind}-mobile.svg')]
    return '<picture>\n'+''.join(f'  <source media="{media}" srcset="assets/{file}">\n' for media,file in sources)+f'  <img src="assets/reference-{kind}.svg" width="1200" alt="{alt}">\n</picture>'


def banner():
    return '## Profile scan\n\n'+picture('profile','Rifatur Rahman — ASCII portrait scanner. AIUB CSE student, C# and ASP.NET Core. Seeking a Full Stack Developer Internship.')


def build():
    d=json.loads((ROOT/'data/cv-profile.json').read_text(encoding='utf-8'))
    s=[banner(),
       "I'm **Rifatur Rahman**, a Computer Science and Engineering student at **American International University-Bangladesh (AIUB)**, based in Dhaka. My main direction is **C# and ASP.NET Core**. I also work with web interfaces, testing, data analysis and AI-assisted systems.",
       '**Seeking a Full Stack Developer Internship** where I can contribute to useful features, learn through code review and build reliable software.',
       f'[Portfolio]({d["portfolio"]}) · [Download CV]({d["cv_url"]}) · [LinkedIn]({d["linkedin"]}) · [Email](mailto:{d["email"]})',
       '## The year, so far',
       picture('activity','GitHub contribution calendar snapshot, 20 October 2026. Includes disclosed synthetic contribution-art commits. Moving object is decorative.'),
       'GitHub snapshot · 20 October 2026. This calendar includes [disclosed synthetic contribution-art commits](https://github.com/rifatur17/contribution-calendar-art); its total is not a measure of genuine development work. The animated crawler does not alter any tile counts.',
       '## Signal',
       picture('signal','Public GitHub snapshot: repository count, calendar contributions, primary repository languages and active days. Includes synthetic art activity.'),
       'Snapshot values are generated from GitHub, rather than live counters. Contribution and active-day values include the disclosed art repository.',
       '## Selected work',
       '### StockPilot — inventory & sales',
       '`C#` · `ASP.NET Core MVC / Web API` · `EF Core` · `SQL Server` · `Bootstrap`',
       'An inventory and sales application connecting purchase receiving, POS, invoices, payments, returns and reports.',
       '- MVC pages and REST endpoints share the same application services.\n- Four Identity roles, account lockout, and role/ownership checks protect workflows.\n- SQL Server application locks, rowversion and persisted operation keys coordinate inventory writes and retries.\n- Unit, integration and browser checks run through GitHub Actions, including SQL Server container coverage.',
       '[Repository](https://github.com/rifatur17/StockPilot-Inventory-Sales-Management) · [Architecture](https://github.com/rifatur17/StockPilot-Inventory-Sales-Management/blob/main/docs/ARCHITECTURE.md) · [Concurrency design](https://github.com/rifatur17/StockPilot-Inventory-Sales-Management/blob/main/docs/INVENTORY_CONCURRENCY.md) · [Screenshot](https://github.com/rifatur17/StockPilot-Inventory-Sales-Management/blob/main/docs/screenshots/dashboard-desktop.png)',
       '### IncidentLens — evidence-based incident investigation',
       '`Python` · `FastAPI` · `LangGraph` · `LangChain` · `Next.js`',
       'An incident-investigation system that connects logs, source changes and deployment evidence through hybrid vector/BM25 retrieval, an investigation workflow and citation checks.',
       '**My contribution:** repository maintenance, dependency security, glob compatibility and CI reliability. The project retains [Niloy Bhuiyan’s upstream authorship](https://github.com/Niloy-Bhuiyan/IncidentLens); the hosted demo belongs to that upstream project.',
       '[Repository](https://github.com/rifatur17/IncidentLens) · [My security change](https://github.com/rifatur17/IncidentLens/commit/ab1025ba8f7e5c571396285971d433f95b228b13) · [Compatibility adapter & tests](https://github.com/rifatur17/IncidentLens/tree/main/tools/eslint-glob-compat)',
       '### Hospital Appointment System — patient & staff workflows',
       '`PHP` · `MySQL` · `HTML` · `CSS` · `JavaScript`',
       'A team MVC project covering patient registration, doctor/specialization management, appointment booking and dashboards, developed through feature branches and pull requests.',
       '**My focus:** patient authentication and doctor administration. Booking and appointment dashboards are part of the wider team contribution. The repository documents the contribution branches and setup status.',
       '[Repository](https://github.com/hospital-appointment-team/hospital-appointment-system) · [My foundation PR](https://github.com/hospital-appointment-team/hospital-appointment-system/pull/1)',
       '### Solar System Simulation — interactive graphics',
       '`C++` · `OpenGL` · `GLUT`',
       'An interactive 3D solar-system simulation with planetary orbits, camera controls and lighting effects.',
       '[Repository](https://github.com/rifatur17/Solar-System-Simulation) · [Source](https://github.com/rifatur17/Solar-System-Simulation/blob/main/main.cpp)',
       'More .NET work: [G Energy — React + ASP.NET Core charging demonstration](https://github.com/rifatur17/G-Energy-Project-Demo).',
       '## Technical toolkit',
       'My core direction is **.NET full-stack development**. The broader technologies below are listed in my CV.',
       '| Area | Technologies |\n| :--- | :--- |\n'+'\n'.join(f'| {area} | {", ".join(tools)} |' for area,tools in d['skills'].items()),
       '## Education',
       f'**{d["university"]}** · {d["location"]}\n\n{d["degree"]} — student',
       '**Relevant coursework:** '+', '.join(d['coursework'])+'.',
       '## Research & analysis',
       '**'+d['research']['title']+'**',
       '**Research team lead · four-person team.** Led work from research design through Python analysis and paper writing for a between-subjects experiment. The analysis uses pandas, SciPy and scikit-learn.',
       '| Study evidence | Reported result |\n| :--- | :--- |\n| Valid participants | 183 |\n| Source-label recall | 50.8% |\n| Consumer-trust prediction | Cross-validated ridge R² = 0.578 |\n| Anti-consumption classification | Cross-validated logistic-regression AUC = 0.879 |',
       'These are study-specific analysis results. The profile does not imply publication acceptance.',
       f'[Research repository]({d["research"]["repo"]}) · [Paper]({d["research"]["paper"]}) · [Analysis results]({d["research"]["results"]})',
       '## Leadership',
       '- **Thesis team lead:** coordinated a four-member team through study design, analysis and writing.\n- **Academic project team lead:** coordinated .NET and Web Technologies projects, assigned tasks and contributed to implementation and delivery.',
       '## Training & workshops',
       '\n'.join(f'- **{item["name"]}**'+(f' ({item["year"]})' if item['year'] else '')+f' — {item["provider"]}' for item in d['training']),
       '## Connect',
       f'[Email](mailto:{d["email"]}) · [LinkedIn]({d["linkedin"]}) · [Portfolio]({d["portfolio"]}) · [CV]({d["cv_url"]})\n\n{d["location"]} · [{d["phone"]}](tel:{d["phone"]})']
    md='\n\n'.join(s)+'\n'
    (ROOT/'README.md').write_text(md,encoding='utf-8',newline='\n')
    transcript=md.replace(banner(),'# Rifatur Rahman — Full-Stack Developer',1).replace('(assets/Rifatur_Rahman_CV.pdf)','(../assets/Rifatur_Rahman_CV.pdf)')
    (ROOT/'docs/PROFILE_TEXT.md').write_text(transcript,encoding='utf-8',newline='\n')
    print('Generated CV-aligned README and searchable transcript.')


if __name__=='__main__':
    build()
