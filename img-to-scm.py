from PIL import Image
from numpy import array
from requests import get


def draw(x, y):
    return f"(px {SCALE[x]} {SCALE[y]})"


URL = f"https://mse.mehvix.com/url-qr.png"
COLOR = '"black"'
QR_SIZE = 23
CANVAS_SIZE = (800 // QR_SIZE) * QR_SIZE
PX = CANVAS_SIZE // QR_SIZE
SCALE = list(range(-QR_SIZE // 2, QR_SIZE // 2))

img = Image.open(get(URL, stream=True).raw)
arr = array(img).tolist()[::-1]  # unflip
moves = []
for y, r in enumerate(arr):
    for x, c in enumerate(r):
        if not c:
            moves.append(draw(x, y))

moves_str = "\n  ".join(moves)
scheme = f"\
;;; Scheme Recursive Art Contest Entry\n\
;;;\n\
;;; Please do not include your name or personal info in this file.\n\
;;;\n\
;;; Title: MSE: MSE Scheme EschQR\n\
;;;\n\
;;; Description:\n\
;;;   <...drawing hands create\n\
;;;    meaningless symbols which form\n\
;;;    strange loops, just as hands...>\n\
\n\
(define (draw)\n\
  (ht)\n\
  (pixelsize {PX})\n\
  {moves_str}\n\
  (exitonclick))\n\
\n\
(define (px x y)\n\
  (pixel x y {COLOR})\n\
)\n\
; Please leave this last line alone.  You may add additional procedures above\n\
; this line.\n\
(draw)\n\
"

with open("contest.scm", "w") as fout:
    fout.write(scheme)
