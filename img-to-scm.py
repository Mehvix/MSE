import qrcode
from PIL import Image
from numpy import array

QR_SIZE = 23
CANVAS_SIZE = (800 // QR_SIZE) * QR_SIZE
PX = CANVAS_SIZE // QR_SIZE
SCALE = list(range(-QR_SIZE // 2, QR_SIZE // 2))

qr = qrcode.QRCode(
    border=1, version=1, error_correction=qrcode.constants.ERROR_CORRECT_L
)
qr.add_data("mse.mehvix.com")
img = qr.make_image(fit=True)
img = img.resize((23, 23), Image.NEAREST)
arr = array(img).tolist()[::-1]  # unmirror

moves = []
for y, r in enumerate(arr):
    for x, c in enumerate(r):
        if not c:
            moves.append(f"(px {SCALE[x]} {SCALE[y]})")

moves_str = "\n  ".join(moves)
with open("contest.scm", "w") as fout:
    fout.write(
        f'\
;;; Scheme Recursive Art Contest Entry\n\
;;;\n\
;;; Please do not include your name or personal info in this file.\n\
;;;\n\
;;; Title: MSE: MSE Scheme EschQR\n\
;;;\n\
;;; Description:\n\
;;;   <...drawing hands create\n\
;;;    a strange loop from meaningless\n\
;;;    symbols, just as hands...>\n\
\n\
(define (draw)\n\
  (ht)\n\
  (pixelsize {PX})\n\
  {moves_str}\n\
  (exitonclick))\n\
\n\
(define (px x y)\n\
  (pixel x y "black")\n\
)\n\
; Please leave this last line alone.  You may add additional procedures above\n\
; this line.\n\
(draw)'
    )
