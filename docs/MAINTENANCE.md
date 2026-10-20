# Profile maintenance

## Current direction

The current direction blends hacker styling with a readable developer portfolio: black/deep-blue surfaces, blue/cyan corner accents, subtle edge code rain, a brief sliced name glitch, and a CV-based developer code window. The main name stays readable. Project-specific workflow diagrams remain the central showcase, with sources and credit visible.

The profile uses 28 variants for seven panels: desktop/mobile and animated/physically static alternatives. `scripts/terminal_showcase.py` defines the terminal framing and identity header, reusing project diagrams from `scripts/showcase_panels.py`. Regenerate through `scripts/build_assets.py`. New `cipher-` image paths avoid GitHub's old image cache.

Matching README assets live in the nine repositories listed in `docs/REPOSITORY_PRESENTATION.md`. Their new `terminal-overview` filenames avoid stale cached visuals. Full CV information, source PDF, project code and original documentation remain intact.

## Content and sources

- `data/cv-profile.json`: current CV-aligned identity, education, technology, contact, research and training data.
- `scripts/build_readme.py`: project narratives, role attribution and page structure.
- `scripts/build_assets.py`: the 28 project-specific showcase variants.
- `assets/Rifatur_Rahman_CV.pdf`: exact supplied CV; preserve its bytes unless a new version is explicitly supplied.
- `docs/CV_RECONCILIATION.md`: source reconciliation and ownership boundaries.
- `docs/PROFILE_SETTINGS.md`: prepared values for native sidebar fields that require account settings access.

`scripts/terminal_showcase.py` defines current identity/framing; `scripts/showcase_panels.py` supplies project diagrams and labels. Older snapshot, ASCII, mint-frame, matrix and prose generators are historical records.

## Regenerate and verify

```powershell
python scripts/build_assets.py
python scripts/build_readme.py
python scripts/validate_profile.py
python scripts/validate_profile.py --links
git diff --check
```

Inspect light/dark desktop/mobile renderings before publication. Keep upstream credit and the separation between project capabilities and personal contribution intact. LinkedIn may reject automated HTTP clients; its destination is taken directly from the supplied CV rather than treated as broken solely because of HTTP 999.

The public profile README is displayed because this public repository matches the account username. Native bio, avatar and social fields are managed separately in GitHub account settings.
