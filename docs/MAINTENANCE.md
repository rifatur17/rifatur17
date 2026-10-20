# Profile design and maintenance

The root README appears on the GitHub profile because this public repository matches the username `rifatur17`.

## Direction

A developer-terminal visual direction: near-black green surfaces, phosphor-green output, cyan syntax accents, monospace typography, window chrome, coordinate grids, and source-oriented schematics. The hero opens with `whoami`, while project figures resemble a trace or a dependency inspector. This reflects the user's requested hacker/dev-console atmosphere without implying cybersecurity credentials or inventing operational data. Each figure explains an implemented boundary or tradeoff rather than displaying invented metrics.

All panels share a circuit/matrix environment generated in `scripts/console_background.py`: green/cyan atmospheric gradients, moving code rain, circuit-edge packets, a traveling light sweep, perspective floor grids, and stepped illuminated corners. Prose panels add a dark center beneath the text so the stronger background stays at the edges. These are authored decorative graphics, not intercepted data or a live security console. GitHub controls the surrounding page and sidebar backgrounds; only repository-rendered assets are styled.

StockPilot leads because it directly supports the stated C#/.NET internship direction. G Energy demonstrates React-to-.NET integration. IncidentLens demonstrates narrowly attributed security and maintenance work. Hospital Appointment System was reviewed but not featured: its public README still describes unmerged contribution branches and pending runtime verification. Other graphics and research work remain discoverable through the portfolio.

## GitHub rendering

- Project descriptions, engineering notes, identity and stack are terminal readouts with staggered text reveal. Every readout has descriptive alt text and a searchable [text-only transcript](PROFILE_TEXT.md). Project headings and navigation remain native Markdown links.
- GitHub-supported `picture` elements select light/dark asset filenames. Both themes deliberately keep the artwork dark, like embedded terminal windows; surrounding text follows GitHub's selected theme.
- All 44 SVGs are local, self-contained vector files, with no scripts, external fonts, foreignObject, or network requests. Native SVG motion moves schematic packets and scanner lines; the header adds code streams, a rotating reticle, a blinking cursor and a name reveal. Readout lines reveal within about three seconds, then remain readable for most of the 24-second cycle. Picture sources select 18 physically animation-free alternatives when reduced motion is requested.
- No dynamic stats services, skill-icon services, custom CSS layouts, or external widgets are required.
- Figures scale to their available width. Below 600px, picture sources select a larger-type header, vertically stacked project diagrams and narrower prose readouts with larger type. Links use native GitHub rendering so every destination remains individually clickable.
- Figure links lead to implementation details. They are conceptual diagrams, not application screenshots or results from a test run.

See GitHub's [profile README requirements](https://docs.github.com/en/account-and-profile/how-tos/profile-customization/managing-your-profile-readme) and [supported picture-element example](https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/quickstart-for-writing-on-github).

## Update

1. Edit prose in `scripts/text_panels.py`, navigation in `scripts/build_readme.py`, or figures in `scripts/build_assets.py`. Keep contribution boundaries explicit.
2. Run `python scripts/build_assets.py` and `python scripts/build_readme.py` to regenerate assets, README and the text-only transcript.
3. Run `python scripts/validate_profile.py` for local checks, or add `--links` to check HTTPS destinations.
4. Preview the README on GitHub in light and dark mode and at a narrow viewport.
5. Commit README and generated assets together. No scheduled workflow is necessary.

The source-review record is in [EVIDENCE.md](EVIDENCE.md). It records inspection, not a new execution of the featured applications' test suites.
