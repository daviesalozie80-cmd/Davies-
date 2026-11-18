"""Banner v4: plain black background with a handwritten "Subscribe" (Kalam, SIL OFL) (2560x1440)."""
import base64, os
HERE = os.path.dirname(os.path.abspath(__file__))
font = base64.b64encode(open(os.path.join(HERE, "assets", "kalam-latin-400-normal.woff2"), "rb").read()).decode()
svg = ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 2560 1440" width="2560" height="1440">'
       f"<style>@font-face{{font-family:'Kalam';font-weight:400;src:url(data:font/woff2;base64,{font}) format('woff2');}}</style>"
       '<rect width="2560" height="1440" fill="#000000"/>'
       '<text x="1280" y="842" text-anchor="middle" font-family="Kalam" font-size="330" '
       'fill="#FFFFFF" stroke="#FFFFFF" stroke-width="5" stroke-linejoin="round">Subscribe</text></svg>')
os.makedirs(os.path.join(HERE, "src"), exist_ok=True)
open(os.path.join(HERE, "src", "banner-black-subscribe-2560x1440.svg"), "w").write(svg)
open(os.path.join(HERE, "src", "banner-black-subscribe-safe-area-guide.svg"), "w").write(svg.replace("</svg>",
    '<rect x="507" y="508" width="1546" height="423" fill="none" stroke="#FF00AA" stroke-width="4" stroke-dasharray="20 10"/></svg>'))
print("built black")
