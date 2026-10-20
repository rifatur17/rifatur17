"""Check README assets, SVG safety and reproducibility; optionally HTTPS links."""
import argparse
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
import re
import urllib.request
import xml.etree.ElementTree as ET

from build_assets import make
from text_panels import make_text

ROOT = Path(__file__).resolve().parents[1]


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--links", action="store_true")
    args = parser.parse_args()
    md = (ROOT / "README.md").read_text(encoding="utf-8")
    assert not re.search(r"<(script|style|iframe)|style=|javascript:", md, re.I)
    paths = re.findall(r'(?:src|srcset)="(assets/[^\"]+)"', md)
    assert len(set(paths)) == 44
    for path in sorted(set(paths)):
        file = ROOT / path
        xml = file.read_text(encoding="utf-8")
        stem=file.stem.removeprefix('cyber-')
        tree = ET.fromstring(xml)
        assert tree.attrib["viewBox"].startswith(("0 0 1200 ", "0 0 720 ", "0 0 600 "))
        assert not re.search(r"<script|<foreignObject|https?://(?!www.w3.org/2000/svg)|onload=|@import", xml, re.I)
        assert 'bg-grid' in xml and 'bg-base' in xml
        if stem.startswith('readout-'):
            animated=not stem.startswith('readout-still-')
            name=stem.removeprefix('readout-').removeprefix('still-')
            narrow=name.endswith('-mobile')
            assert xml == make_text(name.removesuffix('-mobile'),narrow,animated)
            assert ('<animate ' in xml) == animated
            if not animated:
                assert not any(el.tag.rsplit('}',1)[-1].startswith('animate') for el in tree.iter())
            continue
        animated = stem.startswith('motion-')
        if animated:
            assert "prefers-reduced-motion:reduce" in xml
            assert "animateMotion" in xml and "animateTransform" in xml
            kind, theme = stem.removeprefix("motion-").rsplit("-", 1)
        else:
            assert 'animateMotion' not in xml and 'animateTransform' not in xml
            kind, theme = stem.removeprefix('still-'), 'dark'
        narrow = kind.endswith("-mobile")
        assert xml == make(theme, kind.removesuffix("-mobile"), narrow, animated), f"Stale asset: {path}"
    assert len(re.findall(r"<picture>", md)) == len(re.findall(r"</picture>", md)) == 9
    assert all(re.search(r'alt="[^\"]+"', image) for image in re.findall(r"<img\b[^>]+>", md))
    print("PASS: 44 reproducible SVGs; 9 pictures; alt text; animated prose and static alternatives; no scripts or external dependencies.")
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
