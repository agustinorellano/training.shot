"""Genera ../index.html incrustando las imágenes de free-exercise-db.
Uso (desde la raíz del repo):
  git clone --depth 1 https://github.com/yuhonas/free-exercise-db.git /tmp/free-exercise-db
  python3 src/build.py /tmp/free-exercise-db   # requiere Pillow
"""
import re, json, base64, io, sys, pathlib
from PIL import Image
here = pathlib.Path(__file__).parent
db = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else "/tmp/free-exercise-db") / "exercises"
t = (here / "template.html").read_text()
D = {}
for f in sorted(set(re.findall(r"img:'([^']+)'", t))):
    fr = []
    for i in (0, 1):
        im = Image.open(db / f / f"{i}.jpg").convert("RGB")
        im.thumbnail((300, 300))
        b = io.BytesIO(); im.save(b, "JPEG", quality=58, optimize=True)
        fr.append("data:image/jpeg;base64," + base64.b64encode(b.getvalue()).decode())
    D[f] = fr
(here.parent / "index.html").write_text(t.replace("/*IMAGES*/{}", json.dumps(D)))
print(len(D), "imágenes incrustadas")
