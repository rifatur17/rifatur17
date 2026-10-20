"""Black/blue terminal identity and restrained hacker framing for project diagrams."""
from pathlib import Path
from html import escape
import xml.etree.ElementTree as ET
from showcase_panels import make as project_base, KINDS, META
ROOT=Path(__file__).resolve().parents[1]


def atmosphere(w,h,animated):
 p=[f'<defs><clipPath id="cyber-frame"><rect x="2" y="2" width="{w-4}" height="{h-4}" rx="12"/></clipPath><linearGradient id="edge-blue"><stop stop-color="#45caff"/><stop offset=".5" stop-color="#2447a1"/><stop offset="1" stop-color="#8d85ff"/></linearGradient><filter id="packet-glow"><feGaussianBlur stdDeviation="5"/></filter></defs>',f'<g clip-path="url(#cyber-frame)">']
 for i in range(6):
  x=w-12-i*19
  p.append('<g opacity=".13" font-family="Consolas,Courier New,monospace" font-size="11" fill="#58a8ff">')
  for j,t in enumerate(['01','{}','10','//','01']):p.append(f'<text x="{x}" y="{-j*21}">{escape(t)}</text>')
  if animated:p.append(f'<animateTransform attributeName="transform" type="translate" from="0 -80" to="0 {h+140}" dur="{12+i}s" begin="{-i*2}s" repeatCount="indefinite"/>')
  p.append('</g>')
 p.append('</g>')
 for d in [f'M2 38V12Q2 2 12 2H48',f'M{w-48} 2H{w-12}Q{w-2} 2 {w-2} 12V38',f'M2 {h-38}V{h-12}Q2 {h-2} 12 {h-2}H48',f'M{w-48} {h-2}H{w-12}Q{w-2} {h-2} {w-2} {h-12}V{h-38}']:
  p.append(f'<path d="{d}" fill="none" stroke="url(#edge-blue)" stroke-width="2"/>')
 return '\n'.join(p)


def hero(narrow,animated):
 w,h=(600,780) if narrow else (1200,520)
 p=[f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" role="img" aria-labelledby="title desc">','<title id="title">Rifatur Rahman — developer terminal</title>','<desc id="desc">Full-stack developer and AIUB CSE student in Dhaka. C#, ASP.NET Core, web engineering and applied AI. Original black and deep-blue artwork, with decorative code rain and brief glitch accents.</desc>',f'''<defs><linearGradient id="base"><stop stop-color="#020407"/><stop offset="1" stop-color="#071126"/></linearGradient><radialGradient id="halo"><stop stop-color="#265bea" stop-opacity=".3"/><stop offset="1" stop-color="#265bea" stop-opacity="0"/></radialGradient><pattern id="scan" width="6" height="6" patternUnits="userSpaceOnUse"><path d="M0 0H6" stroke="#78a7ff" stroke-opacity=".035"/></pattern><clipPath id="frame"><rect width="{w}" height="{h}" rx="12"/></clipPath></defs><g clip-path="url(#frame)"><rect width="{w}" height="{h}" fill="url(#base)"/><ellipse cx="{w*.76}" cy="{h*.45}" rx="500" ry="400" fill="url(#halo)"/><rect width="{w}" height="{h}" fill="url(#scan)"/></g><rect x="1" y="1" width="{w-2}" height="{h-2}" rx="12" fill="none" stroke="#20365b"/>''',atmosphere(w,h,animated)]
 def text(x,y,t,size=18,color='#eaf1ff',weight=400,mono=False,extra=''):
  family='Consolas,Courier New,monospace' if mono else 'Segoe UI,Arial,sans-serif'
  p.append(f'<text x="{x}" y="{y}" font-family="{family}" font-size="{size}" fill="{color}" font-weight="{weight}" {extra}>{escape(t)}</text>')
 def line(d,color='#263e68'):
  p.append(f'<path d="{d}" fill="none" stroke="{color}"/>')
 x=30 if narrow else 44
 for i,c in enumerate(['#669eff','#3d5386','#1d3157']):p.append(f'<circle cx="{x+i*16}" cy="27" r="3.5" fill="{c}"/>')
 text(x+70,33,'rifatur17 / developer.workspace',14,'#8ba8d1',mono=True)
 line(f'M1 51H{w-1}')
 text(x,97,'[ FULL-STACK / .NET / WEB / AI ]',16,'#64bcff',600,True)
 ny=169 if narrow else 182
 if narrow:
  text(x,ny,'Rifatur',68,weight=750);text(x,ny+76,'Rahman',68,weight=750)
 else:text(x,ny,'Rifatur Rahman',64,weight=750)
 if animated:
  p.append(f'<defs><clipPath id="name-glitch"><rect x="0" y="{ny-42}" width="{w}" height="9"/><rect x="0" y="{ny-9}" width="{w}" height="5"/></clipPath></defs><g clip-path="url(#name-glitch)" opacity="0">')
  text(x+7,ny,'Rifatur' if narrow else 'Rifatur Rahman',68 if narrow else 64,'#67d9ff',750)
  text(x-5,ny,'Rifatur' if narrow else 'Rifatur Rahman',68 if narrow else 64,'#9585ff',750)
  p.append('<animate attributeName="opacity" values="0;0;.7;0;.4;0;0" keyTimes="0;.8;.805;.81;.815;.82;1" dur="14s" repeatCount="indefinite"/></g>')
 sy=291 if narrow else 237
 text(x,sy,'Building interfaces. Designing systems.',23,'#b4c8e8')
 text(x,sy+37,'Exploring applied AI.',23,'#b4c8e8')
 # Visual code window: facts from the CV, no simulated production status.
 bx,by,bw,bh=(30,370,540,284) if narrow else (732,112,424,274)
 p.append(f'<rect x="{bx-8}" y="{by-8}" width="{bw+16}" height="{bh+16}" rx="16" fill="#4781ff" opacity=".07"/><rect x="{bx}" y="{by}" width="{bw}" height="{bh}" rx="10" fill="#030a17" stroke="#36578b"/>')
 text(bx+18,by+29,'~/developer.json',16,'#7dbbff',mono=True)
 line(f'M{bx} {by+44}H{bx+bw}')
 lines=[('{', '#7daeff'),('  "name": "Rifatur Rahman",','#c6dcfa'),('  "focus": "C# / ASP.NET Core",','#88cfff'),('  "build": ["web", "applied AI"],','#c6dcfa'),('  "education": "CSE @ AIUB"','#c6dcfa'),('}', '#7daeff')]
 for i,(t,c) in enumerate(lines):text(bx+18,by+76+i*27,t,17 if narrow else 15,c,mono=True)
 yy=by+bh-19
 text(bx+18,yy,'> build · test · iterate',15,'#6ebaff',mono=True)
 if animated:
  p.append(f'<rect x="{bx+bw-35}" y="{yy-12}" width="8" height="15" fill="#8bceff"><animate attributeName="opacity" values="1;1;0;0" keyTimes="0;.49;.5;1" dur="1.6s" repeatCount="indefinite"/></rect>')
  route=f'M{bx-8} {by+20}V{by+bh+8}H{bx+bw-10}'
  line(route,'#244978');p.append(f'<circle r="4" fill="#8acaff"><animateMotion path="{route}" dur="8s" repeatCount="indefinite"/></circle>')
 fy=698 if narrow else 440
 line(f'M{x} {fy-23}H{w-x}')
 text(x,fy+5,'CSE @ AIUB  /  DHAKA, BANGLADESH',16,'#93b1d8',mono=True)
 text(x,fy+39,'SEEKING A FULL-STACK INTERNSHIP',16,'#80c4ff',600,True)
 p.append('</svg>');return '\n'.join(p)+'\n'


def make(kind,narrow=False,animated=True):
 if kind=='hero':result=hero(narrow,animated)
 else:
  result=project_base(kind,narrow,animated)
  root=ET.fromstring(result);w=int(root.get('width'));h=int(root.get('height'))
  # Darken large surfaces while preserving all original diagram positions/content.
  for old,new in {'#04090f':'#020407','#0b1932':'#071126','#101c31':'#091326','#233858':'#2d4973','#29405f':'#2b4771'}.items():result=result.replace(old,new)
  result=result.replace('rx="18"','rx="12"')
  result=result.replace('</svg>',atmosphere(w,h,animated)+'\n</svg>')
 ET.fromstring(result)
 return result

if __name__=='__main__':
 for kind in KINDS:
  for narrow in (False,True):
   for animated in (False,True):
    name=f"cipher-{'still-' if not animated else ''}{kind}{'-mobile' if narrow else ''}.svg"
    (ROOT/'assets'/name).write_text(make(kind,narrow,animated),encoding='utf-8',newline='\n')
 print('Generated 28 hacker/developer portfolio variants.')
