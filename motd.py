from base64 import b64decode as d6

banner = b'CgoKG1szM20bWzFtCiBfX19fXyAgICAgICAgIF8gICAgIF9fX19fXyAgX19fX19fXyAgX19fX19fICAgX19fX19fX19fICAgX19fX19fICAgICAgIAp8IHwgXCBcICAgICAgIHwgfCAgIC8gfCAgICAgICAgfCB8ICAgLyB8ICB8IFwgfCB8IHwgfCB8IFwgfCB8ICB8IFwgICAgICAKfCB8ICB8IHwgIF8gICB8IHwgICAnLS0tLS0tLiAgIHwgfCAgIHwgfCAgfCB8IHwgfCB8IHwgfCB8IHwgfF9ffF8vICAgICAgCnxffF8vXy8gIHxffF9ffF98ICAgIF9fX198Xy8gICB8X3wgICBcX3xfX3xfLyB8X3wgfF98IHxffCB8X3wgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCgoKCgogX19fX19fICAgX19fX19fICAgICBfX19fX18gIF9fX19fICBfX19fX18gICBfICAgIF8gIF9fX19fX18gIF9fX19fXyAgICAKfCB8ICBcIFwgLyB8ICB8IFwgICB8IHwgIHwgXCAgfCB8ICB8IHwgX19fXyB8IHwgIHwgfCAgIHwgfCAgIC8gfCAgICAgICAgCnwgfCAgfCB8IHwgfCAgfCB8ICAgfCB8X198IHwgIHwgfCAgfCB8ICB8IHwgfCB8LS18IHwgICB8IHwgICAnLS0tLS0tLiAgIAp8X3wgIHxffCBcX3xfX3xfLyAgIHxffCAgXF9cIF98X3xfIHxffF9ffF98IHxffCAgfF98ICAgfF98ICAgIF9fX198Xy8gICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiBfX19fX18gICBfX19fX18gIF9fX19fXyAgIF9fX19fXyAgX19fX19fICAgXyAgICAgXyAgIF9fX19fXyAgX19fX18gICAgIAp8IHwgIHwgXCB8IHwgICAgIC8gfCAgICAgIHwgfCAgICAgfCB8ICB8IFwgfCB8ICAgfCB8IHwgfCAgICAgfCB8IFwgXCAgICAKfCB8X198IHwgfCB8LS0tLSAnLS0tLS0tLiB8IHwtLS0tIHwgfF9ffCB8IFwgXCAgIC8gLyB8IHwtLS0tIHwgfCAgfCB8ICAgCnxffCAgXF9cIHxffF9fX18gIF9fX198Xy8gfF98X19fXyB8X3wgIFxfXCAgXF9cXy9fLyAgfF98X19fXyB8X3xfL18vICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKG1swbQoKCg=='

def show_banner():
    _=[print(f"{ea}{' ' if sleep(0.05) else ''}") for i, ea in enumerate(d6(banner).decode().split("\n"))]