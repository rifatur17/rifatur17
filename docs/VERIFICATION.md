# Published profile verification

Checked on 20 October 2026 (Asia/Dhaka).

## Current terminal revision

Published the terminal redesign in `febfcea5d0a7f0eaa5024e7f1f4a89cd41a868c6`. GitHub's API confirmed that commit on `main`. The art uses dark green terminal surfaces, neon green/cyan, monospace type, window chrome, grids, and implementation schematics. Both GitHub themes deliberately use dark terminal panels.

After publication, all six live Chrome checks were repeated at 1440/390/320px in light and dark color schemes. Each returned HTTP 200, loaded four new `terminal-` SVG assets with nonzero natural widths, selected the correct desktop/mobile source, displayed the internship statement, and had no horizontal document overflow. The actual published dark desktop rendering and desktop/mobile asset sheets were visually reviewed. SVG reproducibility/safety checks, GitHub Markdown rendering, and `git diff --check` also passed. Project destinations and factual claims remain the same as the initial version.

## Initial publication

- Created public `rifatur17/rifatur17` after confirming the repository did not already exist through authenticated access.
- Published README and supporting assets on `main` in commit `6af84cbaddaa1609b31688516a82151c8f5f634f`. GitHub's API and `git ls-remote` independently returned that commit.
- GitHub's Markdown API rendered the README successfully, retaining all four picture elements, media sources, alt text, and project links.
- Local validation parsed all 16 SVG files, checked reproducibility against the generator, and checked for active content and external dependencies.
- All 17 distinct HTTPS destinations in the README returned HTTP 200, including the portfolio, CV, project repositories, source files, and screenshot.
- Live profile browser verification used installed Chrome through Playwright at widths 1440, 390, and 320 in both light and dark color schemes. All six visits returned HTTP 200, displayed the internship statement and four pictures, and loaded all four selected images with nonzero natural widths.
- Desktop visits selected 1200px assets; both mobile widths selected 720px mobile assets in the correct color theme. No horizontal document overflow was detected in any of the six visits.
- Desktop, narrow, light, and dark captures were generated; the desktop light/dark and narrow light layouts were visually inspected. Asset sheets were also visually inspected in both themes.
- `git diff --check` passed. No changes to the featured project repositories or existing portfolio were made.

This is profile-content and rendering verification. The featured applications' test suites were not re-executed as part of this change; their linked test records retain their own scope and dates.

## Account metadata limitation

Repository creation and publication succeeded with the available GitHub credential. A separate `PATCH /user` attempt for the short bio and website field returned HTTP 404. Those account fields were not updated; no credential permissions were changed. The README itself contains the internship statement, portfolio, CV, and public contact email.

Prepared short bio, if account settings are updated separately:

> CSE student at AIUB | C# & ASP.NET Core | Full-stack projects with SQL Server | Seeking a Full Stack Developer Internship

Website: https://rifatur17.github.io/
