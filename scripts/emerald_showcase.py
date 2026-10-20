"""Emerald/teal portfolio with explicit moving objects and reference-inspired panels."""
from pathlib import Path
from html import escape
import colorsys,re,json,copy,math
import xml.etree.ElementTree as ET
from terminal_showcase import make as terminal_base
from showcase_panels import KINDS as PROJECT_KINDS
ROOT=Path(__file__).resolve().parents[1]
KINDS=[*PROJECT_KINDS,'toolkit','stats']
NS='http://www.w3.org/2000/svg'

def recolor(svg):
 def color(m):
  c=m.group()[1:];r,g,b=[int(c[i:i+2],16)/255 for i in (0,2,4)];h,s,v=colorsys.rgb_to_hsv(r,g,b)
  if s<.2 and v>.65:return '#f0f7f3' if v>.9 else '#b6c9c0'
  if v<.22:h,s=.43,min(s,.56)
  else:h=.45 if h<.64 else .41;v=min(v,.94)
  rgb=colorsys.hsv_to_rgb(h,s,v)
  return '#'+''.join(f'{round(a*255):02x}' for a in rgb)
 return re.sub(r'#[0-9a-fA-F]{6}',color,svg)

def motion_objects(w,h,kind,animated):
 p=['<defs><filter id="object-glow"><feGaussianBlur stdDeviation="4"/></filter></defs>']
 # Moving lights trace the frame, giving every repo a visible animated surface.
 route=f'M12 40V{h-18}H{w-18}V18H40'
 if animated:
  for i in range(3):
   for r,opacity in [(8,.24),(3.2,1)]:
    p.append(f'<circle r="{r}" fill="#73f4c8" opacity="{opacity}"'+(' filter="url(#object-glow)"' if r==8 else '')+f'><animateMotion path="{route}" dur="18s" begin="{-i*6}s" repeatCount="indefinite"/></circle>')
 if kind=='hero':
  cx,cy=(490,201) if w==600 else (641,237)
  rx,ry=(54,62) if w==600 else (69,82)
  p.append(f'<ellipse cx="{cx}" cy="{cy}" rx="{rx}" ry="{ry}" fill="none" stroke="#3ee2ae" stroke-opacity=".22" stroke-dasharray="3 7"/>')
  p.append(f'<g transform="translate({cx} {cy})"><g>')
  if animated:p.append('<animateTransform attributeName="transform" type="translate" values="0 -9;0 9;0 -9" dur="4.8s" repeatCount="indefinite"/>')
  p.append('<rect x="-32" y="-25" width="64" height="50" rx="14" fill="#0a211a" stroke="#63edbd" stroke-width="2"/><rect x="-25" y="-17" width="50" height="31" rx="8" fill="#030d09"/><path d="M0 -25V-36M-43 -5h11M32 -5h11M-15 25v9M15 25v9" stroke="#70e6bb" stroke-width="2"/><circle cy="-39" r="4" fill="#c7ffeb"/><text x="0" y="5" text-anchor="middle" font-family="Consolas,Courier New,monospace" font-size="20" fill="#f3fff9">&lt;/&gt;</text></g></g>')
  orbit=f'M{cx-rx} {cy}a{rx} {ry} 0 1 0 {2*rx} 0a{rx} {ry} 0 1 0 {-2*rx} 0'
  for i,s in enumerate(['{}','C#','01']):
   if animated:p.append(f'<g transform="translate({cx-rx} {cy})"><g>')
   else:p.append(f'<g transform="translate({cx+[-rx,0,rx][i]} {cy+[-10,-ry,12][i]})">')
   p.append(f'<rect x="-15" y="-12" width="30" height="24" rx="6" fill="#071a12" stroke="#329b79"/><text x="0" y="5" text-anchor="middle" font-family="Consolas,Courier New,monospace" font-size="13" fill="#c5ffe8">{escape(s)}</text>')
   if animated:p.append(f'<animateMotion path="M0 0a{rx} {ry} 0 1 0 {2*rx} 0a{rx} {ry} 0 1 0 {-2*rx} 0" dur="16s" begin="{-i*5.3}s" repeatCount="indefinite"/>')
   p.append('</g></g>' if animated else '</g>')
 else:
  cx,cy=w-50,40
  p.append(f'<g transform="translate({cx} {cy})"><g>')
  if animated:p.append('<animateTransform attributeName="transform" type="translate" values="0 -5;0 5;0 -5" dur="4s" repeatCount="indefinite"/>')
  p.append('<rect x="-20" y="-15" width="40" height="30" rx="8" fill="#0a211a" stroke="#43c69c"/><text x="0" y="6" text-anchor="middle" font-family="Consolas,Courier New,monospace" font-size="17" fill="#e3fff1">&lt;/&gt;</text></g></g>')
 return '\n'.join(p)

def extra(kind,narrow,animated):
 w=600 if narrow else 1200;h=(650 if narrow else 390) if kind=='toolkit' else (620 if narrow else 390)
 title='Technical toolkit' if kind=='toolkit' else 'GitHub overview'
 p=[f'<svg xmlns="{NS}" width="{w}" height="{h}" viewBox="0 0 {w} {h}" role="img" aria-labelledby="title desc">',f'<title id="title">{title}</title>','<desc id="desc">CV-listed technologies and a dated public repository snapshot. Moving badges and marker lights are decorative.</desc>',f'<rect x="1" y="1" width="{w-2}" height="{h-2}" rx="12" fill="#050e0a" stroke="#245543"/>']
 def text(x,y,s,size=18,color='#edf8f2',weight=400,mono=False):
  family='Consolas,Courier New,monospace' if mono else 'Segoe UI,Arial,sans-serif'
  p.append(f'<text x="{x}" y="{y}" font-size="{size}" fill="{color}" font-weight="{weight}" font-family="{family}">{escape(str(s))}</text>')
 text(28,43,'DEVELOPER / '+('TOOLKIT' if kind=='toolkit' else 'GITHUB SNAPSHOT'),14,'#63e3b6',600,True)
 text(28,90,title,34,weight=700)
 if kind=='toolkit':
  items=[('C#','C#'),('.NET','ASP.NET Core'),('Py','Python'),('TS','TypeScript'),('R','React'),('SQL','SQL Server'),('C++','C++'),('JS','JavaScript'),('Git','Git / CI'),('PHP','PHP'),('5','HTML'),('{}','CSS')]
  cols=3 if narrow else 6;step=184 if narrow else 192;bw=164 if narrow else 176
  for i,(icon,label) in enumerate(items):
   x=28+(i%cols)*step;y=132+(i//cols)*116
   p.append(f'<g transform="translate({x} {y})"><g>')
   if animated:p.append(f'<animateTransform attributeName="transform" type="translate" values="0 -3;0 3;0 -3" dur="{4+i%4}s" begin="{-i*.4}s" repeatCount="indefinite"/>')
   p.append(f'<rect width="{bw}" height="95" rx="12" fill="#0a1b13" stroke="#2b6c52"/><rect x="12" y="12" width="48" height="45" rx="9" fill="#103024" stroke="#388f6b"/>')
   text(17 if len(icon)>3 else (20 if len(icon)>2 else 23),43,icon,18 if len(icon)>2 else 22,'#b6ffe0',700,True);text(12,80,label,17,'#d5eee0')
   p.append('</g></g>')
  text(28,h-20,'Core: C# / ASP.NET Core · complete CV below',15,'#86ae99',mono=True)
 else:
  d=json.loads((ROOT/'data/profile-public-metadata.json').read_text(encoding='utf-8'))
  metrics=[(d['public_repositories'],'PUBLIC REPOS'),(len(d['primary_languages_by_repo']),'REPO LANGUAGES'),(d['showcased_projects'],'SHOWCASED PROJECTS')]
  bw=164 if narrow else 185;step=184 if narrow else 205
  for i,(v,label) in enumerate(metrics):
   x=28+i*step;y=123
   p.append(f'<rect x="{x}" y="{y}" width="{bw}" height="112" rx="12" fill="#0a1b13" stroke="#2b6c52"/>')
   text(x+16,y+55,v,40,'#b4ffe0',700);text(x+16,y+88,label,12,'#94c5ae',mono=True)
  cx,cy=(166,390) if narrow else (815,215);radius=88
  total=sum(d['primary_languages_by_repo'].values());acc=0
  colors=['#43e5b0','#24b99a','#d7fff1','#3c7767']
  lx,ly=(315,324) if narrow else (949,160)
  for i,(label,count) in enumerate(d['primary_languages_by_repo'].items()):
   amount=count/total*(2*math.pi*radius)
   p.append(f'<circle cx="{cx}" cy="{cy}" r="{radius}" fill="none" stroke="{colors[i]}" stroke-width="24" stroke-dasharray="{amount} {2*math.pi*radius-amount}" stroke-dashoffset="{-acc}" transform="rotate(-90 {cx} {cy})"/>')
   p.append(f'<circle cx="{lx}" cy="{ly+i*35-6}" r="4" fill="{colors[i]}"/>');text(lx+14,ly+i*35,f'{label}  {count}',16,'#b9d7c7',mono=True)
   acc+=amount
  text(cx-22,cy+7,str(total),28,'#e5fff0',700)
  text(cx-18,cy+31,'REPOS',11,'#92b7a4',mono=True)
  text(28,270 if narrow else 280,'Primary language per repository',17,'#aacdbc')
  text(28,h-54,'Snapshot: '+d['snapshot_date'],15,'#7fa891',mono=True)
  text(28,h-26,'Dated public metadata · not a skill rating',14,'#7fa891',mono=True)
  if animated:
   path=f'M{cx-111} {cy}a111 111 0 1 0 222 0a111 111 0 1 0 -222 0'
   p.append(f'<circle r="4" fill="#e0fff0"><animateMotion path="{path}" dur="14s" repeatCount="indefinite"/></circle>')
 p.append(motion_objects(w,h,kind,animated));p.append('</svg>');return '\n'.join(p)+'\n'

def make(kind,narrow=False,animated=True):
 if kind in ('toolkit','stats'):result=extra(kind,narrow,animated)
 else:
  source=recolor(terminal_base(kind,narrow,animated))
  # Strengthen edge rain without hiding text or altering diagram facts.
  source=source.replace('opacity=".13" font-family','opacity=".25" font-family')
  tree=ET.fromstring(source);w=int(tree.get('width'));h=int(tree.get('height'))
  if animated and kind!='solar':
   for parent in list(tree.iter()):
    for e in list(parent):
     if e.tag.rsplit('}',1)[-1]!='circle':continue
     motion=next((c for c in e if c.tag.rsplit('}',1)[-1]=='animateMotion'),None)
     if motion is None:continue
     dur=float(motion.get('dur','8s').rstrip('s'))
     for j in (1,2):
      clone=copy.deepcopy(e);clone.set('r','2.5');clone.set('opacity',str(.65-j*.13));cm=next(iter(clone));cm.set('begin',f'{-dur*j/3}s');parent.append(clone)
  ET.register_namespace('',NS);source=ET.tostring(tree,encoding='unicode')
  result=source.replace('</svg>',motion_objects(w,h,kind,animated)+'\n</svg>')
 ET.fromstring(result)
 return result

def make_badge(kind):
 labels={'portfolio':'Portfolio ↗','cv':'Download CV ↓','linkedin':'LinkedIn ↗','email':'Email @'}
 return f'<svg xmlns="{NS}" width="200" height="54" viewBox="0 0 200 54" role="img" aria-label="{labels[kind]}"><rect x="1" y="1" width="198" height="52" rx="10" fill="#0a2118" stroke="#3cb58b"/><text x="100" y="34" text-anchor="middle" font-family="Segoe UI,Arial,sans-serif" font-size="21" font-weight="600" fill="#d8ffeb">{labels[kind]}</text></svg>\n'


if __name__=='__main__':
 for kind in KINDS:
  for narrow in (False,True):
   for animated in (False,True):
    name=f"verdant-{'still-' if not animated else ''}{kind}{'-mobile' if narrow else ''}.svg"
    (ROOT/'assets'/name).write_text(make(kind,narrow,animated),encoding='utf-8',newline='\n')
 for badge in ('portfolio','cv','linkedin','email'):
  (ROOT/'assets'/f'verdant-contact-{badge}.svg').write_text(make_badge(badge),encoding='utf-8',newline='\n')
 print('Generated 36 portfolio variants and 4 native contact badges.')
