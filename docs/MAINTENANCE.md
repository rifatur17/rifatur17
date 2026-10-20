# Profile maintenance

## Current direction

The user selected a blend of cyberpunk hacker styling and a clean premium developer profile. The current design uses a near-black background, neon-green accents, decorative falling glyphs, brief sliced glitch lettering and moving diagram packets. A large readable identity banner leads into four project cards. Both GitHub page themes use the same artwork. Native links and role attribution remain visible; full CV information and engineering notes are in expandable sections.

Twenty SVGs provide desktop/mobile and animated/physically static reduced-motion variants for the hero and four project cards. Important text never disappears. Project illustrations are conceptual, not live telemetry. The surrounding GitHub page and sidebar remain under GitHub's control.

The custom contribution/signal panels are no longer displayed. GitHub's own contribution section remains unchanged, as does the separate contribution-art repository and its disclosure. No commit dates or activity were modified by this redesign.

## Content and sources

- `data/cv-profile.json`: current CV-aligned identity, education, technology, contact, research and training data.
- `scripts/build_readme.py`: project narratives, role attribution and page structure.
- `scripts/build_assets.py`: the twenty neon portfolio variants.
- `assets/Rifatur_Rahman_CV.pdf`: exact supplied CV; preserve its bytes unless a new version is explicitly supplied.
- `docs/CV_RECONCILIATION.md`: source reconciliation and ownership boundaries.
- `docs/PROFILE_SETTINGS.md`: prepared values for native sidebar fields that require account settings access.

`scripts/neon_panels.py` defines current artwork and project labels. Older snapshot, ASCII, mint-frame, matrix and prose generators are historical records.

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
