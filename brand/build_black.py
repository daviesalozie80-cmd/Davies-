"""Banner v4: plain black background with "Subscribe" (2560x1440)."""
import base64, os
HERE = os.path.dirname(os.path.abspath(__file__))
font = base64.b64encode(open(os.path.join(HERE, "assets", "montserrat-latin-900-normal.woff2"), "rb").read()).decode()
svg = ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 2560 1440" width="2560" height="1440">'
       f"<style>@font-face{{font-family:'Montserrat';font-weight:900;src:url(data:font/woff2;base64,{font}) format('woff2');}}</style>"
       '<rect width="2560" height="1440" fill="#000000"/>'
       '<text x="1280" y="809" text-anchor="middle" font-family="Montserrat" font-weight="900" font-size="250" '
       'letter-spacing="2" fill="#FFFFFF">Subscribe</text></svg>')
os.makedirs(os.path.join(HERE, "src"), exist_ok=True)
open(os.path.join(HERE, "src", "banner-black-subscribe-2560x1440.svg"), "w").write(svg)
open(os.path.join(HERE, "src", "banner-black-subscribe-safe-area-guide.svg"), "w").write(svg.replace("</svg>",
    '<rect x="507" y="508" width="1546" height="423" fill="none" stroke="#FF00AA" stroke-width="4" stroke-dasharray="20 10"/></svg>'))
print("built black")
