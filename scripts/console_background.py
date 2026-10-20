"""Shared circuit/matrix atmosphere; purely decorative, no telemetry claims."""


def background(width, height, prose=False):
    p=[f'''<defs>
      <linearGradient id="bg-base" x2="0.8" y2="1"><stop stop-color="#041e18"/><stop offset="0.5" stop-color="#020b09"/><stop offset="1" stop-color="#001614"/></linearGradient>
      <radialGradient id="bg-aura"><stop stop-color="#0c765a" stop-opacity="0.42"/><stop offset="1" stop-color="#00110d" stop-opacity="0"/></radialGradient>
      <pattern id="bg-grid" width="32" height="32" patternUnits="userSpaceOnUse"><path d="M32 0H0V32" fill="none" stroke="#2baf73" stroke-opacity="0.16" stroke-width="0.7"/><circle cx="0" cy="0" r="1" fill="#4fffb1" opacity="0.32"/></pattern>
      <linearGradient id="bg-sweep"><stop stop-color="#65ffc0" stop-opacity="0"/><stop offset="0.95" stop-color="#65ffc0" stop-opacity="0.1"/><stop offset="1" stop-color="#afffe8" stop-opacity="0.45"/></linearGradient>
      <filter id="bg-bloom"><feGaussianBlur stdDeviation="3"/></filter>
      <clipPath id="bg-clip"><rect x="2" y="45" width="{width-4}" height="{height-47}" rx="10"/></clipPath>
    </defs>
    <g clip-path="url(#bg-clip)">
      <rect x="2" y="45" width="{width-4}" height="{height-47}" fill="url(#bg-base)"/>
      <ellipse cx="{width*.88}" cy="{height*.42}" rx="{width*.58}" ry="{height*.78}" fill="url(#bg-aura)"/>
      <rect x="2" y="45" width="{width-4}" height="{height-47}" fill="url(#bg-grid)"/>
    ''']
    # Code rain: deterministic authored glyphs, not generated credentials/logs.
    columns=16 if width>=1000 else 9
    for i in range(columns):
        x=18+i*(width-36)/(columns-1)
        edge=i<2 or i>columns-3
        opacity=0.48 if edge else (0.16 if prose else 0.25)
        glyphs=('01','<>','10','//','{}','01','[]','10')
        p.append(f'<g class="motion" opacity="{opacity}" font-family="Consolas,Courier New,monospace" font-size="13" fill="#4df59b">')
        for j in range(8):
            value=glyphs[(i+j)%len(glyphs)]
            p.append(f'<text x="{x:.1f}" y="{-j*22}" opacity="{1-j*.1:.1f}"'+(' fill="#baffde"' if j==0 else '')+f'>{value.replace("<","&lt;").replace(">","&gt;")}</text>')
        p.append(f'<animateTransform attributeName="transform" type="translate" from="0 -60" to="0 {height+210}" dur="{8+(i%5)*1.7}s" begin="{-i*1.43}s" repeatCount="indefinite"/></g>')
    routes=[f'M14 77H44V{height*.35:.0f}H23V{height-72}H85',f'M{width-14} 89H{width-43}V{height*.38:.0f}H{width-24}V{height-83}H{width-97}',f'M16 {height-51}H{width*.25:.0f}L{width*.25+27:.0f} {height-78}H{width*.65:.0f}L{width*.65+28:.0f} {height-50}H{width-17}']
    for i,d in enumerate(routes):
        p.append(f'<path d="{d}" fill="none" stroke="#2fbc89" stroke-opacity="0.35" stroke-width="1.3"/>')
        p.append(f'<g class="motion"><circle r="7" fill="#6affca" opacity="0.55" filter="url(#bg-bloom)"><animateMotion path="{d}" dur="{9+i*3}s" begin="{-i*2}s" repeatCount="indefinite"/></circle><circle r="2.5" fill="#a1ffe3"><animateMotion path="{d}" dur="{9+i*3}s" begin="{-i*2}s" repeatCount="indefinite"/></circle></g>')
    # Perspective floor and a moving luminous sweep add depth to the common frame.
    horizon=height-95
    for i in range(9):
        x=i*width/8
        target=width/2+(x-width/2)*.22
        p.append(f'<path d="M{x:.0f} {height}L{target:.0f} {horizon}" stroke="#38b77e" stroke-opacity="0.16"/>')
    for y in (height-18,height-41,height-63,height-80):
        p.append(f'<path d="M0 {y}H{width}" stroke="#38b77e" stroke-opacity="0.13"/>')
    p.append(f'<g class="motion"><rect x="-120" y="45" width="120" height="{height-45}" fill="url(#bg-sweep)"/><animateTransform attributeName="transform" type="translate" from="0 0" to="{width+120} 0" dur="13s" repeatCount="indefinite"/></g>')
    if prose:
        # Calm the field beneath glyphs, retaining the busy circuit/rain at the edges.
        p.append(f'<rect x="57" y="105" width="{width-112}" height="{height-160}" rx="3" fill="#020b09" opacity="0.84"/>')
    else:
        p.append(f'<rect x="23" y="68" width="{min(width-46,590)}" height="{min(height-125,330)}" fill="#020b09" opacity="0.32"/>')
    p.append('</g>')
    # Stepped brackets and hard corners, unified across prose and system maps.
    for d in [f'M3 81V47H37',f'M{width-37} 47H{width-3}V81',f'M3 {height-39}V{height-3}H37',f'M{width-37} {height-3}H{width-3}V{height-39}']:
        p.append(f'<path d="{d}" fill="none" stroke="#76ffd0" stroke-opacity="0.8" stroke-width="1.5"/>')
    return '\n'.join(p)
