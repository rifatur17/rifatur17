<picture>
  <source media="(prefers-reduced-motion: reduce) and (max-width: 600px)" srcset="assets/still-header-mobile.svg">
  <source media="(prefers-reduced-motion: reduce)" srcset="assets/still-header.svg">
  <source media="(max-width: 600px) and (prefers-color-scheme: dark)" srcset="assets/motion-header-mobile-dark.svg">
  <source media="(max-width: 600px)" srcset="assets/motion-header-mobile-light.svg">
  <source media="(prefers-color-scheme: dark)" srcset="assets/motion-header-dark.svg">
  <source media="(prefers-color-scheme: light)" srcset="assets/motion-header-light.svg">
    <img src="assets/motion-header-light.svg" width="1200" alt="Rifatur Rahman — full-stack developer terminal. C# / ASP.NET Core / SQL Server. AIUB CSE student seeking a full-stack internship.">
</picture>

I'm **Rifatur Rahman**, a BSc in Computer Science and Engineering student at **American International University-Bangladesh (AIUB)**, based in Dhaka. I build across the interface, API, and database, with a focus on **C# and ASP.NET Core**.

**Seeking a Full Stack Developer Internship.**

[Portfolio](https://rifatur17.github.io/) · [CV](https://rifatur17.github.io/assets/motion-Rifatur_Rahman_CV.pdf) · [Email](mailto:rifaturrahman1131@gmail.com)

## `~/projects`

### 01 / StockPilot

**Inventory and sales, connected from receiving to returns.**

A single-business application with purchase receiving, a point of sale, invoices, payments, and stock movements. MVC and REST API endpoints use the same application services.

<a href="https://github.com/rifatur17/StockPilot-Inventory-Sales-Management/blob/main/docs/INVENTORY_CONCURRENCY.md">
  <picture>
    <source media="(prefers-reduced-motion: reduce) and (max-width: 600px)" srcset="assets/still-stockpilot-mobile.svg">
    <source media="(prefers-reduced-motion: reduce)" srcset="assets/still-stockpilot.svg">
    <source media="(max-width: 600px) and (prefers-color-scheme: dark)" srcset="assets/motion-stockpilot-mobile-dark.svg">
    <source media="(max-width: 600px)" srcset="assets/motion-stockpilot-mobile-light.svg">
    <source media="(prefers-color-scheme: dark)" srcset="assets/motion-stockpilot-dark.svg">
    <source media="(prefers-color-scheme: light)" srcset="assets/motion-stockpilot-light.svg">
    <img src="assets/motion-stockpilot-light.svg" width="1200" alt="StockPilot write path: MVC and API share services; LedgerGate opens a serializable transaction and takes a SQL Server application lock before writing stock and the ledger. Writes are deliberately serialized for a small business workload.">
  </picture>
</a>

**Worth inspecting:** transaction-owned SQL application locking, persisted operation keys for retries, and role/ownership checks. The tradeoff is deliberate write serialization for a small-business workload. No production deployment is claimed.

`C#` · `ASP.NET Core MVC / Web API` · `EF Core` · `SQL Server` · `Bootstrap`

[Repository](https://github.com/rifatur17/StockPilot-Inventory-Sales-Management) · [Write gate source](https://github.com/rifatur17/StockPilot-Inventory-Sales-Management/blob/main/src/StockPilot.Infrastructure/LedgerGate.cs) · [Application screenshot](https://github.com/rifatur17/StockPilot-Inventory-Sales-Management/blob/main/docs/screenshots/dashboard-desktop.png) · [Test strategy](https://github.com/rifatur17/StockPilot-Inventory-Sales-Management/blob/main/docs/TESTING.md)

### 02 / G Energy

**A React interface meets a .NET charging workflow.**

An EV charging demonstration connecting Owner/Driver access, vehicle assignments, reservations, charging sessions, and a demo wallet. The React frontend talks to an ASP.NET Core API backed by SQL Server.

<a href="https://github.com/rifatur17/G-Energy-Project-Demo/blob/main/docs/member4-wallet-payment.md">
  <picture>
    <source media="(prefers-reduced-motion: reduce) and (max-width: 600px)" srcset="assets/still-genergy-mobile.svg">
    <source media="(prefers-reduced-motion: reduce)" srcset="assets/still-genergy.svg">
    <source media="(max-width: 600px) and (prefers-color-scheme: dark)" srcset="assets/motion-genergy-mobile-dark.svg">
    <source media="(max-width: 600px)" srcset="assets/motion-genergy-mobile-light.svg">
    <source media="(prefers-color-scheme: dark)" srcset="assets/motion-genergy-dark.svg">
    <source media="(prefers-color-scheme: light)" srcset="assets/motion-genergy-light.svg">
    <img src="assets/motion-genergy-light.svg" width="1200" alt="G Energy demo workflow: reserve, charge, settle. Driver charging permission is separate from the Owner wallet. Charging, top-ups, payments, and refunds are simulated.">
  </picture>
</a>

**Worth inspecting:** vehicle-specific charging permission, the charging-to-wallet settlement boundary, and protected Admin operations. Charging and money movements are simulated; this is a development project, not a live charging network.

`React` · `TypeScript` · `ASP.NET Core Web API` · `EF Core` · `SQL Server`

[Repository](https://github.com/rifatur17/G-Energy-Project-Demo) · [Access rules](https://github.com/rifatur17/G-Energy-Project-Demo/blob/main/backend/GEnergy.Api/Services/VehicleAccess.cs) · [Settlement source](https://github.com/rifatur17/G-Energy-Project-Demo/blob/main/backend/GEnergy.Api/Services/Wallets/WalletChargingSettlement.cs) · [Verification record](https://github.com/rifatur17/G-Energy-Project-Demo/blob/main/docs/member5-verification.md)

### 03 / IncidentLens

**Maintaining the tooling behind evidence-based incident investigation.**

My work here focuses on **dependency security, glob compatibility, and CI reliability**. The application combines Next.js, FastAPI, hybrid retrieval, and LangGraph to connect incident reports to supporting evidence.

<a href="https://github.com/rifatur17/IncidentLens/tree/main/tools/eslint-glob-compat">
  <picture>
    <source media="(prefers-reduced-motion: reduce) and (max-width: 600px)" srcset="assets/still-incidentlens-mobile.svg">
    <source media="(prefers-reduced-motion: reduce)" srcset="assets/still-incidentlens.svg">
    <source media="(max-width: 600px) and (prefers-color-scheme: dark)" srcset="assets/motion-incidentlens-mobile-dark.svg">
    <source media="(max-width: 600px)" srcset="assets/motion-incidentlens-mobile-light.svg">
    <source media="(prefers-color-scheme: dark)" srcset="assets/motion-incidentlens-dark.svg">
    <source media="(prefers-color-scheme: light)" srcset="assets/motion-incidentlens-light.svg">
    <img src="assets/motion-incidentlens-light.svg" width="1200" alt="IncidentLens maintenance focus: dependency audit, compatibility adapter, regression checks. Preserve glob behavior while bounding expansion resources. Original application by Niloy Bhuiyan; upstream history and authorship retained.">
  </picture>
</a>

**Worth inspecting:** the scoped glob compatibility adapter and regression fixtures, including bounds on nested and expanded patterns. This repository preserves [Niloy Bhuiyan's upstream project](https://github.com/Niloy-Bhuiyan/IncidentLens), history, and MIT attribution; I do not claim original authorship of the application.

`Python / FastAPI` · `Next.js / TypeScript` · `Dependency security` · `GitHub Actions`

[Repository](https://github.com/rifatur17/IncidentLens) · [Adapter and regression tests](https://github.com/rifatur17/IncidentLens/tree/main/tools/eslint-glob-compat) · [My security change](https://github.com/rifatur17/IncidentLens/commit/ab1025ba8f7e5c571396285971d433f95b228b13)

## `cat stack.txt`

- **Interface** → `HTML` `CSS` `JavaScript` `Bootstrap` · React + TypeScript in G Energy
- **Application** → `C#` `ASP.NET Core MVC` `Web API`
- **Data** → `Entity Framework Core` `SQL Server`
- **Verification** → unit / integration / browser checks · `Git` `GitHub Actions`

I'm looking for an internship where I can contribute to full-stack features, learn through code review, and deepen my work with .NET and relational data.

### `connect --next`

[rifaturrahman1131@gmail.com](mailto:rifaturrahman1131@gmail.com) · [Explore the portfolio](https://rifatur17.github.io/projects/)
