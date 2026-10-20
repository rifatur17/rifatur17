# Profile maintenance

## Current direction

The user explicitly chose black + emerald/teal + white. The current design adds visible moving objects: a floating developer companion, three orbiting code badges, frame-tracing lights, particle trails and floating skill tiles. Important identity and CV text remain continuously readable. Project-specific diagrams retain their facts and credit.

The supplied YouTube reference `JEFOzaeEJaw` was inspected at its final-profile review. The corresponding additions are a visible technical toolkit, existing CV contact links and a local GitHub overview with a repository-language donut. No third-party stats service or viewer counter is used. `data/profile-public-metadata.json` records the dated GitHub REST snapshot; repositories without a primary language are excluded from its language distribution. This is repository composition, not skill level or genuine contribution history.

The profile uses 36 self-contained panel variants plus four native contact badges: desktop/mobile and animated/physically static versions of nine panels. `scripts/emerald_showcase.py` is the current generator, reusing the earlier terminal and project diagram modules. Run `scripts/build_assets.py`, `scripts/build_readme.py` and `scripts/validate_profile.py`. New `verdant-` and repository `emerald-overview` filenames avoid stale GitHub image caches.

## Content and sources

- `data/cv-profile.json`: current CV-aligned identity, education, technology, contact, research and training data.
- `scripts/build_readme.py`: project narratives, role attribution and page structure.
- `scripts/build_assets.py`: the 36 emerald portfolio variants.
- `assets/Rifatur_Rahman_CV.pdf`: exact supplied CV; preserve its bytes unless a new version is explicitly supplied.
- `docs/CV_RECONCILIATION.md`: source reconciliation and ownership boundaries.
- `docs/PROFILE_SETTINGS.md`: prepared values for native sidebar fields that require account settings access.

`scripts/emerald_showcase.py` defines the current palette, moving objects, skills and metadata panels; terminal/project modules provide the earlier diagrams. Older snapshot, ASCII, mint-frame, matrix and prose generators are historical records.

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
