"""Black and deep-blue engineering portfolio: decorative motion, readable content."""
from html import escape
from pathlib import Path
import xml.etree.ElementTree as ET
ROOT=Path(__file__).resolve().parents[1]
PROJECTS={
 'stock':('01 / FULL-STACK','StockPilot','Inventory. Sales. Consistent writes.','C# / ASP.NET CORE / SQL SERVER', ['PURCHASE','INVENTORY','SALE']),
 'incident':('02 / APPLIED AI','IncidentLens','Evidence-led incident investigation.','PYTHON / FASTAPI / NEXT.JS',['LOGS','RETRIEVAL','EVIDENCE']),
 'hospital':('03 / TEAM PROJECT','Hospital appointments','Patient access. Doctor administration.','PHP / MYSQL / JAVASCRIPT',['PATIENT','AUTH','DOCTOR']),
 'solar':('04 / COMPUTER GRAPHICS','Solar system','Orbital motion. Interactive 3D.','C++ / OPENGL / GLUT',['SUN','ORBIT','PLANET'])}

def make(kind,narrow=False,animated=True):
 w=600 if narrow else 1200
 h=(660 if narrow else 490) if kind=='hero' else (450 if narrow else 310)
 p=[f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" role="img" aria-labelledby="title desc">',f'<title id="title">{escape("Rifatur Rahman — Full-Stack Developer" if kind=="hero" else PROJECTS[kind][1])}</title>','<desc id="desc">Original neon portfolio illustration. Rain, glitch and moving packets are decorative, not live telemetry.</desc>',f'''<defs><radialGradient id="aura"><stop stop-color="#327dff" stop-opacity=".16"/><stop offset="1" stop-color="#327dff" stop-opacity="0"/></radialGradient><linearGradient id="fade"><stop stop-color="#030609"/><stop offset="1" stop-color="#07152f"/></linearGradient><clipPath id="frame"><rect x="1" y="1" width="{w-2}" height="{h-2}" rx="18"/></clipPath><pattern id="grid" width="36" height="36" patternUnits="userSpaceOnUse"><path d="M36 0H0V36" stroke="#4189ff" stroke-opacity=".065" fill="none"/></pattern><filter id="glow"><feGaussianBlur stdDeviation="4"/></filter></defs>''',f'<g clip-path="url(#frame)"><rect width="{w}" height="{h}" fill="url(#fade)"/><rect width="{w}" height="{h}" fill="url(#grid)"/><ellipse cx="{w-70}" cy="{h*.5}" rx="420" ry="400" fill="url(#aura)"/>']
 def txt(x,y,t,size=18,color='#edf4ff',weight=400,mono=False,extra=''):
  family='Consolas,Courier New,monospace' if mono else 'Segoe UI,Arial,sans-serif'
  p.append(f'<text x="{x}" y="{y}" fill="{color}" font-size="{size}" font-weight="{weight}" font-family="{family}" {extra}>{escape(t)}</text>')
 def line(d,color='#243e66',width=1):
  p.append(f'<path d="{d}" fill="none" stroke="{color}" stroke-width="{width}"/>')
 # Rain remains in the illustration area, never across primary prose.
 if animated:
  for i in range(9):
   x=(w-270+i*31) if not narrow else (322+i*33)
   p.append('<g class="motion" opacity=".22">')
   for j in range(6): txt(x,-j*22,('01','{}','//','10','<>')[(i+j)%5],12,'#4d94ff',mono=True)
   p.append(f'<animateTransform attributeName="transform" type="translate" from="0 -80" to="0 {h+170}" dur="{9+i%3*2}s" begin="{-i*1.7}s" repeatCount="indefinite"/></g>')
 p.append('</g>')
 line(f'M24 1H{w-24}','#2b4c7a')
 line(f'M24 {h-1}H{w-24}','#2b4c7a')
 p.append(f'<rect x="1" y="1" width="{w-2}" height="{h-2}" rx="18" fill="none" stroke="#243b60"/>')
 if kind=='hero':
  x=32 if narrow else 48
  txt(x,45,'R / R     SOFTWARE ENGINEERING',15,'#75adff',600,True)
  line(f'M{x} 67H{w-x}','#192d4d')
  ny=153 if narrow else 171
  if narrow:
   txt(x,ny,'Rifatur',70,weight=750);txt(x,ny+78,'Rahman',70,weight=750)
  else: txt(x,ny,'Rifatur Rahman',68,weight=750)
  # Glitch ghosts flash briefly; the base name is always readable.
  if animated:
   p.append(f'<defs><clipPath id="glitch-slice"><rect x="0" y="{ny-49}" width="{w}" height="13"/><rect x="0" y="{ny-15}" width="{w}" height="6"/></clipPath></defs><g clip-path="url(#glitch-slice)" opacity="0" class="motion">')
   txt(x+8,ny,'Rifatur' if narrow else 'Rifatur Rahman',70 if narrow else 68,'#4a8eff',750)
   txt(x-5,ny,'Rifatur' if narrow else 'Rifatur Rahman',70 if narrow else 68,'#91b7ff',750)
   p.append('<animate attributeName="opacity" values="0;0;.8;0;.6;0;0" keyTimes="0;.73;.735;.74;.745;.75;1" dur="10s" repeatCount="indefinite"/><animateTransform attributeName="transform" type="translate" values="0 0;0 0;8 0;-5 0;3 0;0 0;0 0" keyTimes="0;.73;.735;.74;.745;.75;1" dur="10s" repeatCount="indefinite"/></g>')
  ry=284 if narrow else 221
  txt(x,ry,'FULL-STACK DEVELOPER',24 if narrow else 25,'#6aa6ff',600,True)
  txt(x,ry+48,'.NET systems. Thoughtful interfaces.',23,'#afbed4')
  txt(x,ry+82,'Applied AI. Built with curiosity.',23,'#afbed4')
  footer=h-102
  line(f'M{x} {footer}H{w-x}')
  p.append(f'<circle cx="{x+5}" cy="{footer+36}" r="5" fill="#6aa6ff"/>')
  txt(x+22,footer+42,'SEEKING A FULL-STACK INTERNSHIP',16,'#ddeaff',600,True)
  txt(x,footer+76,'CSE @ AIUB  /  DHAKA, BANGLADESH',14,'#879fbe',mono=True)
  # Abstract terminal: a compact code composition, not a repeated portrait.
  bx,by,bw,bh=(32,407,536,105) if narrow else (817,110,335,260)
  p.append(f'<rect x="{bx}" y="{by}" width="{bw}" height="{bh}" rx="10" fill="#050c1b" stroke="#31588c"/>')
  if narrow:
   txt(bx+18,by+31,'> build --with-intent',17,'#70acff',mono=True)
   txt(bx+18,by+65,'C#   /   WEB   /   AI',21,mono=True)
   route=f'M{bx+18} {by+85}H{bx+bw-18}'
  else:
   for i,c in enumerate(['#6aa6ff','#27436a','#27436a']): p.append(f'<circle cx="{bx+20+i*16}" cy="{by+20}" r="3" fill="{c}"/>')
   txt(bx+19,by+64,'> developer.init()',17,'#6aa6ff',mono=True)
   for i,(label,val) in enumerate([('focus','".NET"'),('interface','"WEB"'),('explore','"AI"')]):
    txt(bx+21,by+106+i*38,label,16,'#8ba1bf',mono=True);txt(bx+151,by+106+i*38,val,18,'#ebf4ff',mono=True)
   route=f'M{bx+21} {by+222}H{bx+bw-21}'
 else:
  category,title,subtitle,stack,nodes=PROJECTS[kind]
  x=28 if narrow else 36
  txt(x,43,category,14,'#7bb3ff',600,True)
  txt(x,96,title,32 if narrow else 36,weight=700)
  txt(x,138,subtitle,19 if narrow else 22,'#b6c5dc')
  txt(x,183,stack,15,'#8daee0',mono=True)
  if narrow: bx,by,bw=28,240,544
  else: bx,by,bw=800,96,355
  if kind=='solar':
   cx,cy=bx+bw/2,by+(65 if narrow else 28)
   for radius in [39,66,94]: p.append(f'<ellipse cx="{cx}" cy="{cy}" rx="{radius*1.5}" ry="{radius*.65}" fill="none" stroke="#274a7b"/>')
   p.append(f'<circle cx="{cx}" cy="{cy}" r="13" fill="#a6ceff"/>')
   route=f'M{cx-99} {cy}a99 43 0 1 0 198 0a99 43 0 1 0 -198 0'
  else:
   gap=14;boxw=(bw-2*gap)/3
   for i,n in enumerate(nodes):
    xx=bx+i*(boxw+gap)
    p.append(f'<rect x="{xx}" y="{by}" width="{boxw}" height="70" rx="8" fill="#0a1932" stroke="#3564a2"/>')
    txt(xx+boxw/2,by+41,n,14 if narrow else 11,'#b8d6ff',600,True,'text-anchor="middle"')
    if i<2: line(f'M{xx+boxw} {by+35}h{gap}','#6aa6ff')
   route=f'M{bx} {by+94}H{bx+bw}'
  line(f'M{x} {h-65}H{w-x}','#1b3154')
  label={'stock':'SHARED SERVICES  /  WRITE COORDINATION','incident':'CONTRIBUTION  /  SECURITY + CI','hospital':'MY FOCUS  /  AUTH + DOCTOR ADMIN','solar':'INTERACTIVE ORBITS  /  CAMERA + LIGHTING'}[kind]
  txt(x,h-29,label,14 if narrow else 15,'#8ba1c1',mono=True)
 # A small traveling packet provides purposeful motion within the visual.
 line(route,'#294a78',1.5)
 if animated:
  p.append(f'<circle r="8" fill="#4c93ff" opacity=".3" filter="url(#glow)"><animateMotion path="{route}" dur="6s" repeatCount="indefinite"/></circle><circle r="3" fill="#b8d8ff"><animateMotion path="{route}" dur="6s" repeatCount="indefinite"/></circle>')
 else:
  pass
 p.append('</svg>')
 result='\n'.join(p)+'\n'
 ET.fromstring(result)
 return result

if __name__=='__main__':
 for kind in ['hero',*PROJECTS]:
  for narrow in (False,True):
   for animated in (False,True):
    name=f"neon-{'still-' if not animated else ''}{kind}{'-mobile' if narrow else ''}.svg"
    (ROOT/'assets'/name).write_text(make(kind,narrow,animated),encoding='utf-8',newline='\n')
 print('Generated 20 neon portfolio assets.')
