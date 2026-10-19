"""Check README assets, SVG safety and reproducibility; optionally HTTPS links."""
import argparse
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
import re
import urllib.request
import xml.etree.ElementTree as ET

from build_assets import make

ROOT = Path(__file__).resolve().parents[1]


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--links", action="store_true")
    args = parser.parse_args()
    md = (ROOT / "README.md").read_text(encoding="utf-8")
    assert not re.search(r"<(script|style|iframe)|style=|javascript:", md, re.I)
    paths = re.findall(r'(?:src|srcset)="(assets/[^\"]+)"', md)
    assert len(set(paths)) == 16
    for path in sorted(set(paths)):
        file = ROOT / path
        xml = file.read_text(encoding="utf-8")
        tree = ET.fromstring(xml)
        assert tree.attrib["viewBox"].startswith(("0 0 1200 ", "0 0 720 "))
        assert not re.search(r"<script|<foreignObject|https?://(?!www.w3.org/2000/svg)|onload=|@import", xml, re.I)
        kind, theme = file.stem.removeprefix("terminal-").rsplit("-", 1)
        narrow = kind.endswith("-mobile")
        assert xml == make(theme, kind.removesuffix("-mobile"), narrow), f"Stale asset: {path}"
    assert len(re.findall(r"<picture>", md)) == len(re.findall(r"</picture>", md)) == 4
    assert all(re.search(r'alt="[^\"]+"', image) for image in re.findall(r"<img\b[^>]+>", md))
    print("PASS: 16 parseable, reproducible, self-contained SVGs; 4 pictures; image alt text; no unsupported active content.")
    if args.links:
        urls = sorted(set(re.findall(r'https://[^\s)"<>]+', md)))
        def check(url):
            req = urllib.request.Request(url, headers={"User-Agent": "rifatur17-profile-link-check"})
            try:
                with urllib.request.urlopen(req, timeout=35) as res:
                    res.read(128)
                    return url, res.status, None
            except Exception as ex:
                return url, None, str(ex)
        with ThreadPoolExecutor(max_workers=4) as pool:
            results = list(pool.map(check, urls))
        for url, status, err in results:
            print(f"{status or 'FAIL'} {url}" + (f" — {err}" if err else ""))
        assert all(status == 200 for _, status, _ in results), "Some links need review."
        print(f"PASS: {len(urls)} HTTPS destinations.")


if __name__ == "__main__":
    main()
