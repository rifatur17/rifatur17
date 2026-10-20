"""Project-specific blue portfolio diagrams; animations are explanatory illustrations."""
from pathlib import Path
from html import escape
import xml.etree.ElementTree as ET
ROOT=Path(__file__).resolve().parents[1]
KINDS=['hero','stock','incident','hospital','solar','energy','research']
META={
 'stock':('StockPilot','Inventory & sales · shared .NET services','C#  /  ASP.NET CORE  /  EF CORE  /  SQL SERVER'),
 'incident':('IncidentLens','Evidence-led investigation · security & CI contribution','PYTHON  /  FASTAPI  /  LANGGRAPH  /  NEXT.JS'),
 'hospital':('Hospital Appointment System','Team project · my focus: authentication & doctor administration','PHP  /  MYSQL  /  JAVASCRIPT'),
 'solar':('Solar System Simulation','Interactive orbits, camera controls and lighting','C++  /  OPENGL  /  GLUT'),
 'energy':('G Energy','Charging demonstration · React + ASP.NET Core','REACT  /  ASP.NET CORE'),
 'portfolio':('Rifatur Rahman / Portfolio','Selected software, AI and research work','SOFTWARE  /  WEB  /  RESEARCH'),
 'test':('GitHub test workspace','A small repository for GitHub experiments','EXPERIMENTS  /  VERSION CONTROL'),
 'art':('Contribution calendar art','Synthetic contribution art · explicitly disclosed','SYNTHETIC DATES  /  VISUAL EXPERIMENT'),
 'research':('Unnoticed Disclosure','AI source labels · research design and Python analysis','PYTHON  /  PANDAS  /  SCIPY  /  SCIKIT-LEARN')}

def make(kind,narrow=False,animated=True):
 w=600 if narrow else 1200
 h=(650 if narrow else 400) if kind=='hero' else ((900 if narrow else 600) if kind=='stock' else ((620 if narrow else 510) if kind in ('incident','hospital') else ((620 if narrow else 480) if kind=='solar' else (530 if narrow else 440))))
 p=[f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" role="img" aria-labelledby="title desc">',f'<title id="title">{escape("Rifatur Rahman — .NET, web and applied AI" if kind=="hero" else META[kind][0])}</title>','<desc id="desc">Original project illustration. Moving states and particles explain a workflow, not live service status or measured test results.</desc>',f'''<defs><linearGradient id="bg"><stop stop-color="#04090f"/><stop offset="1" stop-color="#0b1932"/></linearGradient><radialGradient id="aura"><stop stop-color="#2865c7" stop-opacity=".22"/><stop offset="1" stop-color="#2865c7" stop-opacity="0"/></radialGradient><pattern id="dots" width="18" height="18" patternUnits="userSpaceOnUse"><circle cx="1" cy="1" r=".7" fill="#7aaaff" opacity=".12"/></pattern><clipPath id="frame"><rect x="1" y="1" width="{w-2}" height="{h-2}" rx="18"/></clipPath></defs><g clip-path="url(#frame)"><rect width="{w}" height="{h}" fill="url(#bg)"/><ellipse cx="{w*.82}" cy="{h*.45}" rx="450" ry="400" fill="url(#aura)"/><rect width="{w}" height="{h}" fill="url(#dots)"/></g><rect x="1" y="1" width="{w-2}" height="{h-2}" rx="18" fill="none" stroke="#233858"/>''']
 def text(x,y,s,size=18,color='#e9f2ff',weight=400,mono=False,anchor=None):
  family='Consolas,Courier New,monospace' if mono else 'Segoe UI,Arial,sans-serif'
  align=f' text-anchor="{anchor}"' if anchor else ''
  p.append(f'<text x="{x}" y="{y}" font-family="{family}" font-size="{size}" fill="{color}" font-weight="{weight}"{align}>{escape(s)}</text>')
 def rect(x,y,ww,hh,fill='#0b1425',stroke='#29405f',radius=10):
  p.append(f'<rect x="{x}" y="{y}" width="{ww}" height="{hh}" rx="{radius}" fill="{fill}" stroke="{stroke}"/>')
 def line(d,color='#426596',sw=1.4,dash=''):
  p.append(f'<path d="{d}" fill="none" stroke="{color}" stroke-width="{sw}"'+(f' stroke-dasharray="{dash}"' if dash else '')+'/>')
 def packet(path,dur=7,begin=0,color='#87bcff'):
  line(path,'#294c7d')
  if animated: p.append(f'<circle r="4" fill="{color}"><animateMotion path="{path}" dur="{dur}s" begin="{begin}s" repeatCount="indefinite"/></circle>')
 def phase(x,y,ww,hh,delay=0):
  if animated:p.append(f'<rect x="{x}" y="{y}" width="{ww}" height="{hh}" rx="7" fill="#1b58ab" opacity="0"><animate attributeName="opacity" values="0;.52;0;0" keyTimes="0;.15;.3;1" dur="10s" begin="{delay}s" repeatCount="indefinite"/></rect>')
 def nodes(labels,x,y,bw,gap=18):
  n=len(labels);nw=(bw-gap*(n-1))/n
  for i,label in enumerate(labels):
   xx=x+i*(nw+gap);rect(xx,y,nw,58);phase(xx,y,nw,58,-i*2)
   text(xx+nw/2,y+35,label,17 if narrow else 16,'#c8e1ff',600,True,'middle')
   if i<n-1: packet(f'M{xx+nw} {y+29}h{gap}',3,-i)
  return y+58
 if kind=='hero':
  x=32 if narrow else 48
  text(x,53,'—  .NET  /  WEB ENGINEERING  /  APPLIED AI',14 if narrow else 17,'#91baff',600,True)
  if narrow:
   text(x,134,'Rifatur',62,weight=750);text(x,205,'Rahman',62,weight=750)
   text(x,251,'Full-stack development,',25,'#bdcde4');text(x,288,'from interface to database.',25,'#bdcde4')
   gx,gy,gw=32,341,536
  else:
   text(x,154,'Rifatur Rahman',62,weight=750)
   text(x,211,'Full-stack development,',28,'#bdcde4');text(x,250,'from interface to database.',28,'#bdcde4')
   gx,gy,gw=772,113,380
  nodes(['UI','API','SQL'],gx,gy,gw)
  text(gx,gy+99,'MVC / React → .NET → EF Core',17,'#92b7e7',mono=True)
  packet(f'M{gx} {gy+124}H{gx+gw}',8)
  if narrow:
   text(x,584,'CSE @ AIUB  ·  DHAKA',19,'#b8cce5',mono=True)
   text(x,619,'SEEKING A FULL-STACK INTERNSHIP',16,'#82b7ff',600,True)
  else:
   line('M48 307H1152','#223856')
   text(x,354,'CSE @ AIUB  ·  DHAKA, BANGLADESH',17,'#a2b8d5',mono=True)
   text(748,354,'SEEKING A FULL-STACK INTERNSHIP',16,'#91baff',600,True)
 else:
  title,subtitle,stack=META[kind]
  text(28,42,('FEATURED / FULL-STACK' if kind=='stock' else 'PROJECT / '+kind.upper()),14,'#83b5ff',600,True)
  text(28,95,title,31 if narrow else 38,weight=700)
  if narrow and kind in ['hospital','incident']:
   subtitle=('Team project · authentication' if kind=='hospital' else 'Evidence-led incident investigation')
  text(28,132,subtitle,19 if narrow else 22,'#afc2dc')
  top=166
  if kind=='stock':
   ax,ay,aw,ah=(28,top,544,260) if narrow else (28,top,560,280)
   bx,by,bw,bh=(28,448,544,270) if narrow else (610,top,562,280)
   rect(ax,ay,aw,ah,'#101c31');text(ax+18,ay+32,'INVENTORY / WRITE LIFECYCLE',16,'#a3cbff',600,True)
   cols=12;size=29 if narrow else 30;gap=9
   for i in range(48):
    xx=ax+18+(i%cols)*(size+gap); yy=ay+55+(i//cols)*38
    p.append(f'<rect x="{xx}" y="{yy}" width="{size}" height="24" rx="4" fill="#163052" stroke="#335983">')
    if animated:p.append(f'<animate attributeName="fill" values="#163052;#67a6ff;#163052" dur="10s" begin="{-i*.16}s" repeatCount="indefinite"/>')
    p.append('</rect>')
   text(ax+18,ay+ah-20,'receive → stock → POS → invoice',18,'#c6dfff',mono=True)
   rect(bx,by,bw,bh,'#101c31');text(bx+18,by+32,'RETRY / PERSISTED OPERATION KEY',16,'#a3cbff',600,True)
   for i,(label,detail) in enumerate([('REQUEST','operation key'),('COORDINATE','SQL lock + rowversion'),('RETRY','look up persisted result')]):
    yy=by+55+i*58;rect(bx+18,yy,bw-36,48,'#08101d');phase(bx+18,yy,bw-36,48,-i*3)
    text(bx+32,yy+30,label,15,'#7eb1ff',600,True);text(bx+163,yy+30,detail,16 if narrow else 18,'#d3e4fb',mono=True)
   packet(f'M{bx+bw-20} {by+56}V{by+227}',7)
   text(28,762 if narrow else 477,'SQL application locks  ·  rowversion',18,'#b3cdec',mono=True)
   text(28,797 if narrow else 508,'Persisted keys  ·  shared MVC / API services',17,'#b3cdec',mono=True)
  elif kind=='incident':
   rect(28,top,w-56,250 if narrow else 160,'#101c31')
   if narrow:
    nodes(['LOGS','CODE','DEPLOY'],48,top+24,w-96)
    nodes(['RETRIEVE','REASON','CITE'],48,top+134,w-96)
    packet(f'M{w-64} {top+82}V{top+134}',5)
   else:
    nodes(['LOGS','RETRIEVAL','WORKFLOW','CITATIONS'],48,top+41,w-96,22)
   text(28,top+(310 if narrow else 205),'MY WORK / dependency security + CI',18,'#9ec8ff',600,True)
   text(28,top+(348 if narrow else 241),'Upstream project: Niloy Bhuiyan',17,'#a7bbd6',mono=True)
  elif kind=='hospital':
   rect(28,top,w-56,250 if narrow else 160,'#101c31')
   labels=['SIGN IN','ROLE CHECK','DOCTOR ADMIN']
   if narrow:
    for i,label in enumerate(labels):
     yy=top+17+i*73;rect(48,yy,w-96,55,'#08101d');phase(48,yy,w-96,55,-i*3);text(70,yy+34,label,19,'#c6dfff',600,True)
    packet(f'M{w-66} {top+20}V{top+218}',8)
   else:nodes(labels,48,top+41,w-96,22)
   text(28,top+(310 if narrow else 205),'PATIENT AUTH + DOCTOR ADMINISTRATION',16 if narrow else 18,'#9ec8ff',600,True)
   text(28,top+(348 if narrow else 241),'Booking / dashboards: wider team work',17,'#a7bbd6',mono=True)
  elif kind=='solar':
   rect(28,top,w-56,280 if narrow else 180,'#101c31')
   cx=w/2;cy=top+(138 if narrow else 88)
   p.append(f'<circle cx="{cx}" cy="{cy}" r="17" fill="#a7caff"/><circle cx="{cx}" cy="{cy}" r="29" fill="#36639b" opacity=".3"/>')
   for i,(rx,ry) in enumerate([(88,30),(150,52),(220,77)]):
    line(f'M{cx-rx} {cy}a{rx} {ry} 0 1 0 {2*rx} 0a{rx} {ry} 0 1 0 {-2*rx} 0','#315687')
    path=f'M{cx-rx} {cy}a{rx} {ry} 0 1 0 {2*rx} 0a{rx} {ry} 0 1 0 {-2*rx} 0'
    if animated:p.append(f'<circle r="{5+i*2}" fill="{["#a7d4ff","#6b9fff","#d4e4ff"][i]}"><animateMotion path="{path}" dur="{8+i*7}s" begin="{-i*3}s" repeatCount="indefinite"/></circle>')
    else:p.append(f'<circle cx="{cx-rx}" cy="{cy}" r="{5+i*2}" fill="#9cbfff"/>')
   text(28,top+(327 if narrow else 222),'ORBITS  /  CAMERA  /  LIGHTING',18,'#a3cbff',600,True)
  elif kind=='energy':
   rect(28,top,w-56,250 if narrow else 170,'#101c31')
   nodes(['REACT','API','CHARGING'],48,top+32,w-96,18)
   text(48,top+135,'Charging workflow demonstration',20,'#b9d4f6',mono=True)
   packet(f'M48 {top+160}H{w-48}',7)
  elif kind=='research':
   rect(28,top,w-56,250 if narrow else 170,'#101c31')
   nodes(['DESIGN','ANALYSIS','RESULTS'],48,top+32,w-96,18)
   text(48,top+137,'183 participants · Python analysis',18,'#bdd5f5',mono=True)
  else:
   rect(28,top,w-56,250 if narrow else 170,'#101c31')
   labels={'portfolio':['WORK','DETAILS','CONTACT'],'test':['EXPLORE','CHECK','LEARN'],'art':['DATES','ART','DISCLOSURE']}[kind]
   nodes(labels,48,top+40,w-96,18)
   if kind=='art':text(48,top+139,'Synthetic commits, not genuine work',18,'#bdd5f5',mono=True)
  line(f'M28 {h-80}H{w-28}','#29405f')
  text(28,h-47,stack,14 if narrow else 16,'#94b4e0',mono=True)
  text(28,h-18,'PROJECT WORKFLOW / ILLUSTRATION',11 if narrow else 12,'#7f94b2',mono=True)
 p.append('</svg>');result='\n'.join(p)+'\n';ET.fromstring(result);return result

if __name__=='__main__':
 for kind in KINDS:
  for narrow in (False,True):
   for animated in (False,True):
    name=f"showcase-{'still-' if not animated else ''}{kind}{'-mobile' if narrow else ''}.svg"
    (ROOT/'assets'/name).write_text(make(kind,narrow,animated),encoding='utf-8',newline='\n')
 print('Generated 28 project-specific showcase assets.')
