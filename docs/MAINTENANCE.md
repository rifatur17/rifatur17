# Profile design and maintenance

The root README appears on the GitHub profile because this public repository matches the username `rifatur17`.

## Direction

A developer-terminal visual direction: near-black green surfaces, phosphor-green output, cyan syntax accents, monospace typography, window chrome, coordinate grids, and source-oriented schematics. The hero opens with `whoami`, while project figures resemble a trace or a dependency inspector. This reflects the user's requested hacker/dev-console atmosphere without implying cybersecurity credentials or inventing operational data. Each figure explains an implemented boundary or tradeoff rather than displaying invented metrics.

StockPilot leads because it directly supports the stated C#/.NET internship direction. G Energy demonstrates React-to-.NET integration. IncidentLens demonstrates narrowly attributed security and maintenance work. Hospital Appointment System was reviewed but not featured: its public README still describes unmerged contribution branches and pending runtime verification. Other graphics and research work remain discoverable through the portfolio.

## GitHub rendering

- Ordinary Markdown carries every important claim, project name, stack, and destination. The README remains useful when images fail.
- GitHub-supported `picture` elements select light/dark asset filenames. Both themes deliberately keep the artwork dark, like embedded terminal windows; surrounding text follows GitHub's selected theme.
- All 24 SVGs are local, self-contained vector files, with no scripts, external fonts, foreignObject, or network requests. Native SVG motion moves schematic packets and scanner lines; the header adds code streams, a rotating reticle, and a blinking cursor. All motion is decorative. Picture sources select eight physically animation-free alternatives when `prefers-reduced-motion: reduce` is set; animated files also contain a defensive reduced-motion style. Project text remains stationary and readable.
- No dynamic stats services, skill-icon services, custom CSS layouts, or external widgets are required.
- Figures scale to their available width. Below 600px, picture sources select a larger-type header and vertically stacked project diagrams. Body text and links use GitHub's native responsive rendering; surrounding text also carries the figures' meaning.
- Figure links lead to implementation details. They are conceptual diagrams, not application screenshots or results from a test run.

See GitHub's [profile README requirements](https://docs.github.com/en/account-and-profile/how-tos/profile-customization/managing-your-profile-readme) and [supported picture-element example](https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/quickstart-for-writing-on-github).

## Update

1. Edit README text and keep contribution boundaries explicit.
2. If changing figures, edit `scripts/build_assets.py`, then run `python scripts/build_assets.py`.
3. Run `python scripts/validate_profile.py` for local checks, or add `--links` to check HTTPS destinations.
4. Preview the README on GitHub in light and dark mode and at a narrow viewport.
5. Commit README and generated assets together. No scheduled workflow is necessary.

The source-review record is in [EVIDENCE.md](EVIDENCE.md). It records inspection, not a new execution of the featured applications' test suites.
