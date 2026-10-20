"""Generate the twelve self-contained mint reference panels."""
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]

if __name__=='__main__':
    from profile_scan import make_scan
    for kind in ('profile','activity','signal'):
        for narrow in (False,True):
            for animated in (False,True):
                name=f"reference-{'still-' if not animated else ''}{kind}{'-mobile' if narrow else ''}.svg"
                (ROOT/'assets'/name).write_text(make_scan(kind,narrow,animated),encoding='utf-8',newline='\n')
    print('Generated 12 mint reference panels.')
