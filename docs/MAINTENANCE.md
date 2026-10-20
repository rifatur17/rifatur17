# Profile maintenance

## Current direction

Midnight Studio is a restrained navy/indigo theme with blue/cyan accents, readable native Markdown and one original architecture banner. The banner has desktop/mobile, light/dark and physically static reduced-motion variants. All important identity, skills, education, projects, research, leadership and contact text is immediately readable and searchable. No third-party stats widget, code rain, synthetic-activity metric, delayed prose animation or external font is required.

## Content and sources

- `data/cv-profile.json`: current CV-aligned identity, education, technology, contact, research and training data.
- `scripts/build_readme.py`: project narratives, role attribution and page structure.
- `scripts/build_assets.py`: the eight original banner variants.
- `assets/Rifatur_Rahman_CV.pdf`: exact supplied CV; preserve its bytes unless a new version is explicitly supplied.
- `docs/CV_RECONCILIATION.md`: source reconciliation and ownership boundaries.
- `docs/PROFILE_SETTINGS.md`: prepared values for native sidebar fields that require account settings access.

The older snapshot/ASCII source data and generator modules are historical records; they do not drive the current README.

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
