# Profile maintenance

## Current direction

The current presentation takes inspiration from the supplied Ashfak-Hossain GitHub reference: cohesive project-specific diagrams, a prominent featured project, concise prose and visible source links. Black/deep-blue surfaces and blue accents remain. Motion illustrates each project's workflow rather than repeating a decorative scanner.

Twenty-eight SVGs provide desktop/mobile and animated/static variants for the hero, four main projects, G Energy and research. Full CV information and engineering notes remain in expandable native sections. Credit and contribution boundaries remain visible. These are explanatory illustrations, not production measurements or live service status.

Matching local artwork is also published in the project repositories. Each repository uses four SVGs under `.github/showcase/` and a picture header in README.md, followed by its original documentation. See `docs/REPOSITORY_PRESENTATION.md` for coverage. The generator also supports portfolio, test and synthetic-art headers; those do not become featured development projects on the profile.

## Content and sources

- `data/cv-profile.json`: current CV-aligned identity, education, technology, contact, research and training data.
- `scripts/build_readme.py`: project narratives, role attribution and page structure.
- `scripts/build_assets.py`: the 28 project-specific showcase variants.
- `assets/Rifatur_Rahman_CV.pdf`: exact supplied CV; preserve its bytes unless a new version is explicitly supplied.
- `docs/CV_RECONCILIATION.md`: source reconciliation and ownership boundaries.
- `docs/PROFILE_SETTINGS.md`: prepared values for native sidebar fields that require account settings access.

`scripts/showcase_panels.py` defines current artwork and project labels. Older snapshot, ASCII, mint-frame, matrix and prose generators are historical records.

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
