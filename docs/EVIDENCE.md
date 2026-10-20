# Source review — 20 October 2026 (Asia/Dhaka)

Only profile files were changed. Project repositories and the existing portfolio were read without modification.

## Identity and destinations

- User supplied: Rifatur Rahman, AIUB BSc CSE student, Full Stack Developer Internship goal, core .NET stack.
- [Public GitHub profile](https://github.com/rifatur17): name, Dhaka location, existing C#/ASP.NET bio; seven public repositories at inspection.
- Profile repository `rifatur17/rifatur17` returned 404 through the authenticated account before implementation. No existing profile README or assets needed replacement.
- [Portfolio](https://rifatur17.github.io/) returned HTTP 200 through direct HTTPS. Its [profile data](https://github.com/rifatur17/rifatur17.github.io/blob/main/src/data.ts) supplied the public email, CV destination, and contribution descriptions.
- Portfolio and GitHub list differing LinkedIn slugs. Neither was selected; portfolio, CV, and the already public portfolio email provide a consistent contact path without guessing which social account is current.

## StockPilot

Inspected public main at `fa519bcd3a1e4b99260b31057457c71e186b1f0b`.

- [README](https://github.com/rifatur17/StockPilot-Inventory-Sales-Management/blob/fa519bcd3a1e4b99260b31057457c71e186b1f0b/README.md): features, project responsibilities, test strategy, screenshot provenance, limitations, no production deployment.
- [LedgerGate.cs](https://github.com/rifatur17/StockPilot-Inventory-Sales-Management/blob/fa519bcd3a1e4b99260b31057457c71e186b1f0b/src/StockPilot.Infrastructure/LedgerGate.cs): serializable transaction, exclusive transaction-owned SQL Server application lock, fresh reads after clearing the change tracker, commit/rollback boundary.
- [Inventory concurrency](https://github.com/rifatur17/StockPilot-Inventory-Sales-Management/blob/fa519bcd3a1e4b99260b31057457c71e186b1f0b/docs/INVENTORY_CONCURRENCY.md): persisted actor/key/fingerprint retry semantics, deliberate serialized writes, SQLite evidence limitation.

## G Energy

Inspected public main at `6b28ae497cb1c6fc46b7e5546f5da5690f0b195e`.

- [README](https://github.com/rifatur17/G-Energy-Project-Demo/blob/6b28ae497cb1c6fc46b7e5546f5da5690f0b195e/README.md): React/TypeScript, ASP.NET Core, SQL Server, reservations, roles, Admin workflows; charging and payment simulation.
- [VehicleAccess.cs](https://github.com/rifatur17/G-Energy-Project-Demo/blob/6b28ae497cb1c6fc46b7e5546f5da5690f0b195e/backend/GEnergy.Api/Services/VehicleAccess.cs): active owner and assigned driver/CanCharge checks.
- [WalletChargingSettlement.cs](https://github.com/rifatur17/G-Energy-Project-Demo/blob/6b28ae497cb1c6fc46b7e5546f5da5690f0b195e/backend/GEnergy.Api/Services/Wallets/WalletChargingSettlement.cs): charging finalization delegates to wallet settlement.
- WalletService.cs: transaction scope, owner checks, SQL row locking, simulated refund policy.

The profile describes this repository's implemented workflow without claiming sole authorship of every module or a production deployment.

## IncidentLens

Inspected public main at `ab1025ba8f7e5c571396285971d433f95b228b13`.

- [README](https://github.com/rifatur17/IncidentLens/blob/ab1025ba8f7e5c571396285971d433f95b228b13/README.md): upstream origin, preserved MIT attribution, synthetic corpus, in-process vector index, deployment boundaries.
- backend/app/retrieval/engine.py: deterministic feature-hash vectors, cosine search, BM25 implementation.
- [Compatibility adapter documentation](https://github.com/rifatur17/IncidentLens/blob/ab1025ba8f7e5c571396285971d433f95b228b13/tools/eslint-glob-compat/README.md): scoped dependency boundary, regression fixtures, nesting/output limits.
- GitHub commit records attribute recent dependency, CI, compatibility, and output-bound maintenance changes to Rifatur Rahman. The profile links the inspected final security commit and explicitly credits original application author Niloy Bhuiyan.

No benchmark numbers, production-performance guarantees, or ownership of the upstream deployment are claimed in the profile.

## Other reviewed material

[Hospital Appointment System](https://github.com/hospital-appointment-team/hospital-appointment-system): public README describes PHP/MySQL MVC, separately owned team contributions, unmerged PRs, and runtime verification pending. It was omitted from the primary selection to keep the profile focused on inspectable .NET work and attributable maintenance.

The two user-supplied photographs informed the emphasis on project storytelling and evidence. No reference portrait, branding, project claims, or visual assets were reused.

## Later video references / public data scan

- [Contribution automation tutorial](https://www.youtube.com/watch?v=3brBa0Grkh8): title, description and playback inspected. It concerns automatic daily commits and a green contribution graph. This implementation takes the contribution-grid presentation cue; it does not install or run that automation.
- [GitSkins profile short](https://www.youtube.com/shorts/SJUqhtjIRgU): playback frames showed an ASCII portrait profile-scan composition, contribution-grid animation and a profile-signal panel. Those concepts informed original local SVG assets; no template, third-party visual asset or subscription was used.
- `data/github-public-snapshot.json` stores the real public REST/GraphQL result inspected on 20 October 2026: 8 public repositories, 4 primary repository languages, 84 contribution events across 5 active days in 365 distinct calendar dates. Daily counts reconcile exactly to the GraphQL total. The UI labels the snapshot date.
- The ASCII glyph data is derived from the account's actual public avatar at the `avatar_url` recorded in the snapshot. The avatar was visually inspected before deriving the glyph representation.
