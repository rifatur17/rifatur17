"""Original profile-scan, signal and activity panels from verified public data."""
from html import escape
from pathlib import Path
import json
import xml.etree.ElementTree as ET
from console_background import background

ROOT=Path(__file__).resolve().parents[1]


def make_scan(kind, narrow=False, animated=True):
    data=json.loads((ROOT/'data/github-public-snapshot.json').read_text(encoding='utf-8'))
    w=600 if narrow else 1200
    h={'profile':1100 if narrow else 640,'activity':690 if narrow else 430,'signal':510 if narrow else 315}[kind]
    titles={'profile':'Rifatur Rahman — ASCII profile scan','activity':'Real GitHub contribution activity — animated scan','signal':'Profile signal — verified GitHub snapshot'}
    p=[f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" role="img" aria-labelledby="title desc">',f'<title id="title">{titles[kind]}</title>',f'<desc id="desc">Public GitHub data snapshot as of 20 October 2026. Decorative motion does not change activity counts. {data["public_repositories"]} public repositories, {data["calendar"]["totalContributions"]} contributions in the 365-day calendar.</desc>',f'<rect x="1" y="1" width="{w-2}" height="{h-2}" rx="10" fill="#050d0b" stroke="#214d38"/>',background(w,h),'<style>@keyframes blink{0%,48%{opacity:1}49%,100%{opacity:0}}.cursor{animation:blink 1.6s step-end infinite}@media(prefers-reduced-motion:reduce){.motion{display:none}.cursor{animation:none}}</style>']
    reveal_count=0
    def text(x,y,s,size=20,color='#dff8e9',weight=400,reveal=False):
        nonlocal reveal_count
        if reveal:
            idx=reveal_count
            reveal_count+=1
            start=.01+idx*.006
            end=start+.1
            p.append(f'<defs><clipPath id="typed-{idx}"><rect x="{x}" y="{y-size-4}" width="{w-x-20}" height="{size+12}"><animate attributeName="width" values="0;0;{w-x-20};{w-x-20}" keyTimes="0;{start};{end};1" dur="24s" repeatCount="indefinite"/></rect></clipPath></defs><g clip-path="url(#typed-{idx})">')
        p.append(f'<text x="{x}" y="{y}" font-family="Consolas,Courier New,monospace" font-size="{size}" font-weight="{weight}" fill="{color}">{escape(str(s))}</text>')
        if reveal:
            p.append('</g>')
    def box(x,y,bw,bh):
        p.append(f'<rect x="{x}" y="{y}" width="{bw}" height="{bh}" rx="5" fill="#04120e" fill-opacity="0.92" stroke="#2a5b42"/>')
    for i,c in enumerate(['#396048','#467b59','#71ffaf']):
        p.append(f'<circle cx="{22+i*17}" cy="23" r="4" fill="{c}"/>')
    text(91,29,f'rifatur17 / {kind}.scan',16,'#9eb7ab')
    p.append(f'<path d="M1 44H{w-1}" stroke="#214d38"/>')
    if kind=='profile':
        text(28,94,'$ scan rifatur17 --profile',23 if narrow else 26,'#69e5ed')
        bx,by,bw,bh=(28,123,544,437) if narrow else (28,124,443,440)
        box(bx,by,bw,bh)
        text(bx+15,by+25,'AVATAR / ASCII',14,'#71ffaf')
        art=json.loads((ROOT/'data/avatar-ascii.json').read_text(encoding='utf-8'))
        ax=100 if narrow else 48
        ay=168
        artw=400 if narrow else 402
        for i,row in enumerate(art['rows']):
            p.append(f'<text xml:space="preserve" x="{ax}" y="{ay+i*7.2:.1f}" textLength="{artw}" lengthAdjust="spacingAndGlyphs" font-family="Consolas,Courier New,monospace" font-size="7.8" fill="#85ffc3">{escape(row)}</text>')
        p.append(f'<defs><clipPath id="portrait-scan"><rect x="{bx+2}" y="{by+35}" width="{bw-4}" height="{bh-38}"/></clipPath><linearGradient id="portrait-beam" x2="0" y2="1"><stop stop-color="#7dffd1" stop-opacity="0"/><stop offset="1" stop-color="#afffe8" stop-opacity="0.4"/></linearGradient></defs>')
        p.append(f'<g class="motion" clip-path="url(#portrait-scan)"><g><rect x="{bx}" y="{by+35}" width="{bw}" height="45" fill="url(#portrait-beam)"/><path d="M{bx} {by+80}h{bw}" stroke="#b5ffe8" stroke-width="1.4"/><animateTransform attributeName="transform" type="translate" values="0 -50;0 {bh-70};0 -50" dur="9s" repeatCount="indefinite"/></g></g>')
        x=30 if narrow else 510
        y=620 if narrow else 169
        text(x,y,'Rifatur Rahman',42,'#e5fff0',700,True)
        text(x,y+39,'@rifatur17',23,'#71ffaf')
        fields=[('ROLE','Full Stack Developer'),('STACK','C# / ASP.NET Core / SQL'),('EDUCATION','AIUB / BSc CSE student'),('LOCATION','Dhaka, Bangladesh'),('SEEKING','Full Stack Developer Internship')]
        for i,(label,value) in enumerate(fields):
            yy=y+87+i*(69 if narrow else 62)
            text(x,yy,label,16,'#71ffaf')
            text(x,yy+26,value,24 if narrow else 23,reveal=True)
        if narrow:
            text(30,1080,'UI → API → DATABASE',24,'#69e5ed')
        else:
            text(510,596,'UI → API → DATABASE',25,'#69e5ed')
            text(29,605,'// portrait: public GitHub avatar',14,'#9eb7ab')
        p.append(f'<rect class="cursor" x="{w-49}" y="{h-25}" width="22" height="6" fill="#71ffaf"/>')
    elif kind=='activity':
        weeks=data['calendar']['weeks'][-13:] if narrow else data['calendar']['weeks']
        text(28,95,'$ inspect contribution.activity',23 if narrow else 26,'#69e5ed')
        total=data['calendar']['totalContributions']
        text(28,142,f'{total} contributions / 365 days',26 if narrow else 29,'#e5fff0',700)
        text(28,180 if narrow else 174,'Grid: latest 13 weeks' if narrow else '21 OCT 2025 → 20 OCT 2026 / actual daily counts',18,'#9eb7ab')
        step=39 if narrow else 20
        size=29 if narrow else 14
        gx,gy=(48,208) if narrow else (65,202)
        colors=['#102d20','#175e38','#208d50','#46c577','#8bffc0']
        max_count=max(day['contributionCount'] for week in data['calendar']['weeks'] for day in week['contributionDays'])
        for col,week in enumerate(weeks):
            for day in week['contributionDays']:
                count=day['contributionCount']
                level=0 if not count else min(4,1+(count*3//max(1,max_count)))
                x,y=gx+col*step,gy+day['weekday']*step
                p.append(f'<rect x="{x}" y="{y}" width="{size}" height="{size}" rx="2" fill="{colors[level]}" stroke="#2a5b42" stroke-width="0.5"><title>{day["date"]}: {count} contributions</title></rect>')
        path=f'M{gx} {gy+7*step+21}H{gx+(len(weeks)-1)*step+size}'
        p.append(f'<path d="{path}" stroke="#347453" stroke-dasharray="3 7"/>')
        # The white/cyan crawler is decorative; it never changes actual heatmap fills.
        p.append(f'<g class="motion"><g><path d="M-24 0H-12M-35 0H-30" stroke="#71ffaf" stroke-width="3"/><path d="M12 0L-8 -7L-4 0L-8 7Z" fill="#d5fff5" stroke="#69e5ed"/><animateMotion path="{path}" dur="12s" repeatCount="indefinite"/></g></g>')
        yy=568 if narrow else 399
        text(28,yy,'Snapshot / 20 OCT 2026',20 if narrow else 16,'#71ffaf')
        text(28,yy+37 if narrow else yy+20,'Tiles = real counts; crawler = visual.',19 if narrow else 14,'#9eb7ab')
        if narrow:
            text(28,654,'Full-year calendar linked below ↗',20,'#69e5ed')
    else:
        text(28,94,'$ inspect profile.signal',25,'#69e5ed')
        active=sum(day['contributionCount']>0 for week in data['calendar']['weeks'] for day in week['contributionDays'])
        metrics=[(data['public_repositories'],'PUBLIC REPOS'),(data['calendar']['totalContributions'],'CONTRIBUTIONS / 365D'),(len(data['primary_languages']),'REPO LANGUAGES'),(active,'ACTIVE DAYS / 365D')]
        for i,(value,label) in enumerate(metrics):
            x=28+(i%2)*280 if narrow else 28+i*292
            y=126+(i//2)*157 if narrow else 125
            bw=264 if narrow else 268
            box(x,y,bw,135 if narrow else 128)
            text(x+18,y+62,value,49,'#71ffaf',700)
            text(x+18,y+99,label,17 if narrow else 16,'#dff8e9')
        text(28,473 if narrow else 289,'GitHub snapshot / 20 OCT 2026',19 if narrow else 17,'#9eb7ab')
    p.append('</svg>')
    result='\n'.join(p)+'\n'
    if not animated:
        ET.register_namespace('', 'http://www.w3.org/2000/svg')
        tree=ET.fromstring(result)
        for parent in tree.iter():
            for child in list(parent):
                if child.tag.rsplit('}',1)[-1] in ('style','animate','animateTransform','animateMotion') or child.attrib.get('class')=='motion':
                    parent.remove(child)
        result=ET.tostring(tree,encoding='unicode')+'\n'
    return result
