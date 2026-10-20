"""Mint terminal frame inspired by the user-supplied video reference."""
def background(width,height):
    return f'''<defs>
<linearGradient id="frame" x1="0" y1="0" x2="1" y2="1"><stop stop-color="#123b33"/><stop offset=".28" stop-color="#4a927e"/><stop offset=".53" stop-color="#0e2b25"/><stop offset="1" stop-color="#397e70"/></linearGradient>
<radialGradient id="aura"><stop stop-color="#7df7cf" stop-opacity=".2"/><stop offset="1" stop-color="#7df7cf" stop-opacity="0"/></radialGradient>
<linearGradient id="rim"><stop stop-color="#b5ffe2"/><stop offset=".5" stop-color="#3f7a68"/><stop offset="1" stop-color="#b0f8db"/></linearGradient>
</defs>
<rect x="2" y="2" width="{width-4}" height="{height-4}" rx="12" fill="url(#frame)"/>
<ellipse cx="{width*.25}" cy="{height*.82}" rx="{width*.5}" ry="{height*.6}" fill="url(#aura)"/>
<rect x="13" y="44" width="{width-26}" height="{height-57}" rx="9" fill="#071512" stroke="url(#rim)" stroke-width="2"/>
<path d="M30 {height-6}H{width-30}" stroke="#baffdf" stroke-opacity=".6"/>
'''
