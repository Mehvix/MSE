from PIL import Image
import numpy as np


def draw(x, y):
    return f"(px {SCALE[x]} {SCALE[y]})"


# todo clean this whole file up later
FNAME = "url-qr.png"
COLOR = '"black"'
QR_SIZE = 23
CANVAS_SIZE = 800
PX = CANVAS_SIZE // QR_SIZE
SCALE = list(range(-QR_SIZE // 2, QR_SIZE // 2))
print(SCALE)

img = Image.open(FNAME)
arr = np.array(img).tolist()
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
;;; Title: MSE: MSE Scheme Eschqr\n\
;;;\n\
;;; Description:\n\
;;;   <strange loop emerging\n\
;;;    from a series of symbols\n\
;;;    that form another>\n\
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
