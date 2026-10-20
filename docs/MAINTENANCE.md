# Profile maintenance

## Current direction

The current reference is the user-supplied YouTube Short `SJUqhtjIRgU`: mint terminal frames, ASCII portrait scanning, an animated contribution crawler and signal cards. Three panels each have desktop/mobile and animated/static variants (12 SVGs). Both GitHub page themes use the same dark mint artwork, matching the reference. CV facts and project credit remain native Markdown.

The contribution data is a dated GitHub API snapshot, not live telemetry. It includes the separate disclosed synthetic contribution-art repository. Do not present those values as genuine work or remove the visible disclosure. The surrounding GitHub page and native sidebar are controlled by GitHub.

## Content and sources

- `data/cv-profile.json`: current CV-aligned identity, education, technology, contact, research and training data.
- `scripts/build_readme.py`: project narratives, role attribution and page structure.
- `scripts/build_assets.py`: the twelve reference panel variants.
- `assets/Rifatur_Rahman_CV.pdf`: exact supplied CV; preserve its bytes unless a new version is explicitly supplied.
- `docs/CV_RECONCILIATION.md`: source reconciliation and ownership boundaries.
- `docs/PROFILE_SETTINGS.md`: prepared values for native sidebar fields that require account settings access.

`data/github-public-snapshot.json` and `data/avatar-ascii.json` drive `scripts/profile_scan.py`; `scripts/reference_frame.py` defines the mint frame. Older matrix and prose modules are historical records.

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
