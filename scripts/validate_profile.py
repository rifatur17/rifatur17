"""Validate source fidelity, local assets and optionally public HTTPS destinations."""
from pathlib import Path
import argparse
import hashlib
import json
import re
import urllib.request
from concurrent.futures import ThreadPoolExecutor
import xml.etree.ElementTree as ET
from profile_scan import make_scan

ROOT=Path(__file__).resolve().parents[1]


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--links',action='store_true')
    args=parser.parse_args()
    d=json.loads((ROOT/'data/cv-profile.json').read_text(encoding='utf-8'))
    md=(ROOT/'README.md').read_text(encoding='utf-8')
    paths=set(re.findall(r'(?:src|srcset)="(assets/[^\"]+)"',md))
    assert len(paths)==12
    for name in paths:
        p=ROOT/name
        xml=p.read_text(encoding='utf-8')
        tree=ET.fromstring(xml)
        assert not re.search(r'<script|<foreignObject|https?://(?!www.w3.org/2000/svg)|onload=|@import',xml,re.I)
        stem=p.stem.removeprefix('reference-')
        animated=not stem.startswith('still-')
        stem=stem.removeprefix('still-')
        narrow=stem.endswith('-mobile')
        kind=stem.removesuffix('-mobile')
        assert xml==make_scan(kind,narrow,animated)
        if not animated:
            assert not any(e.tag.rsplit('}',1)[-1].startswith('animate') for e in tree.iter())
    assert hashlib.sha256((ROOT/d['cv']).read_bytes()).hexdigest()==d['cv_sha256']
    for key in ('name','email','phone','linkedin','portfolio','degree','university'):
        assert d[key] in md,key
    assert all(item in md for tools in d['skills'].values() for item in tools)
    assert all(item['name'] in md for item in d['training'])
    assert 'upstream authorship' in md and 'My contribution:' in md and 'My focus:' in md
    assert not re.search(r'<script|<style|style=',md,re.I)
    assert all(re.search(r'alt="[^\"]+"',i) for i in re.findall(r'<img\b[^>]+>',md))
    print('PASS: 12 reproducible safe SVGs; static alternatives; exact supplied CV bytes; CV fields/skills/training; explicit contribution credit.')
    if args.links:
        urls=sorted(set(re.findall(r'https://[^\s)"<>]+',md)))
        def check(url):
            try:
                with urllib.request.urlopen(urllib.request.Request(url,headers={'User-Agent':'rifatur-profile-validation'}),timeout=35) as r:
                    r.read(128)
                    return url,r.status,None
            except Exception as ex:
                return url,None,str(ex)
        with ThreadPoolExecutor(max_workers=4) as pool:
            results=list(pool.map(check,urls))
        for url,status,error in results:
            print(f'{status or "CHECK"} {url}'+(f' — {error}' if error else ''))
        public=[row for row in results if 'linkedin.com' not in row[0]]
        assert all(status==200 for _,status,_ in public),'A public destination needs review.'
        print(f'Checked {len(urls)} HTTPS destinations; LinkedIn restrictions, if any, are reported separately.')


if __name__=='__main__':
    main()
