"""Generate the Midnight Studio banner. Self-contained SVG; no external services."""
from html import escape
from pathlib import Path
import xml.etree.ElementTree as ET

ROOT=Path(__file__).resolve().parents[1]


def make(theme='dark',narrow=False,animated=True):
    dark=theme=='dark'
    bg,panel,ink,muted,line,blue,cyan=('#07111f','#0c1e36','#f2f7ff','#a4b8d2','#233d5e','#78aaff','#75e2de') if dark else ('#f5f8ff','#ffffff','#122a49','#4d6585','#cfdaeb','#285dc1','#007b82')
    w,h=(600,580) if narrow else (1200,440)
    p=[f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" role="img" aria-labelledby="title desc">','<title id="title">Rifatur Rahman — Full-Stack Developer</title>','<desc id="desc">AIUB Computer Science and Engineering student. .NET applications, web engineering and applied AI. Seeking a Full Stack Developer Internship.</desc>',f'<defs><radialGradient id="aura"><stop stop-color="{blue}" stop-opacity="0.22"/><stop offset="1" stop-color="{bg}" stop-opacity="0"/></radialGradient><linearGradient id="edge"><stop stop-color="{blue}"/><stop offset="1" stop-color="{cyan}"/></linearGradient><clipPath id="frame"><rect width="{w}" height="{h}" rx="20"/></clipPath></defs>',f'<g clip-path="url(#frame)"><rect width="{w}" height="{h}" fill="{bg}"/><ellipse cx="{w-110}" cy="80" rx="420" ry="330" fill="url(#aura)"/>']
    for i in range(5):
        x=w-470+i*70
        p.append(f'<path d="M{x} 0L{x+170} {h}" stroke="{line}" stroke-opacity="0.3"/>')
    p.append('</g>')
    def text(x,y,s,size,color=ink,weight=400,mono=False,tracking=None):
        family='Consolas,Courier New,monospace' if mono else 'Segoe UI,Arial,sans-serif'
        track=f' letter-spacing="{tracking}"' if tracking else ''
        p.append(f'<text x="{x}" y="{y}" fill="{color}" font-family="{family}" font-size="{size}" font-weight="{weight}"{track}>{escape(s)}</text>')
    def path(d,stroke=line,sw=1):
        p.append(f'<path d="{d}" stroke="{stroke}" stroke-width="{sw}" fill="none"/>')
    if narrow:
        x=30
        text(x,49,'RR / SOFTWARE ENGINEERING',19,blue,600,True)
        text(x,126,'Rifatur',65,ink,700)
        text(x,197,'Rahman',65,ink,700)
        text(x,247,'Full-Stack Developer',29,blue,600)
        text(x,301,'.NET applications.',26,muted)
        text(x,337,'Web engineering. Applied AI.',26,muted)
        path('M30 376H570')
        for i,(title,detail) in enumerate([('UI','React / MVC'),('API','ASP.NET Core'),('DATA','EF Core / SQL')]):
            xx=30+i*185
            text(xx,419,title,18,cyan,600,True)
            text(xx,450,detail,19,muted)
            if i<2:
                path(f'M{xx+143} 413h25',blue,1.5)
        p.append(f'<rect x="30" y="490" width="540" height="56" rx="9" fill="{panel}" stroke="{line}"/>')
        text(48,525,'SEEKING A FULL-STACK INTERNSHIP',22,ink,500,True)
        route='M30 470H570'
    else:
        text(48,55,'RR / SOFTWARE ENGINEERING',17,blue,600,True,'1.3')
        text(44,144,'Rifatur Rahman',70,ink,700)
        text(48,193,'Full-Stack Developer',30,blue,600)
        text(48,253,'.NET applications. Web engineering.',24,muted)
        text(48,289,'Applied AI, grounded in evidence.',24,muted)
        for i,(title,detail) in enumerate([('INTERFACE','React / MVC'),('APPLICATION','ASP.NET Core'),('DATA','EF Core / SQL Server')]):
            yy=91+i*83
            p.append(f'<rect x="805" y="{yy}" width="345" height="66" rx="9" fill="{panel}" stroke="{line}"/>')
            p.append(f'<rect x="805" y="{yy+13}" width="3" height="40" rx="1" fill="{blue if i!=2 else cyan}"/>')
            text(826,yy+25,title,13,cyan,600,True,'1')
            text(826,yy+49,detail,20,ink,500)
            if i<2:
                path(f'M977 {yy+66}v17',blue,1.5)
        path('M48 353H1152')
        text(48,397,'CSE @ AIUB',19,muted,500,True)
        text(384,397,'SEEKING A FULL-STACK INTERNSHIP',19,ink,500,True)
        text(1066,397,'DHAKA',17,muted,500,True)
        route='M977 157V174M977 240V257'
    if animated:
        p.append(f'<g class="motion"><circle r="4" fill="{cyan}"><animateMotion path="{route}" dur="8s" repeatCount="indefinite"/></circle></g>')
    p.append(f'<path d="M20 {h-2}H{w-20}" stroke="url(#edge)" stroke-width="2"/>')
    p.append('</svg>')
    result='\n'.join(p)+'\n'
    if not animated:
        ET.register_namespace('', 'http://www.w3.org/2000/svg')
        result=ET.tostring(ET.fromstring(result),encoding='unicode')+'\n'
    return result


if __name__=='__main__':
    for theme in ('dark','light'):
        for narrow in (False,True):
            for animated in (False,True):
                name=f"studio-{'still-' if not animated else ''}{theme}{'-mobile' if narrow else ''}.svg"
                (ROOT/'assets'/name).write_text(make(theme,narrow,animated),encoding='utf-8',newline='\n')
    print('Generated 8 Midnight Studio banner variants.')
