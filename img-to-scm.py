from PIL import Image
import numpy as np

FNAME = "url-qr.png"
COLOR = '"black"'

img = Image.open(FNAME)
arr = np.array(img).tolist()

moves = []
x, y = 0, 0


def goto(x, y):
    return f"(goto {x} {y})"


def draw(x, y):
    return f"(pixel {x} {y} {COLOR})"


# todo verify x,y are in right order
for y, r in enumerate(arr):
    for x, c in enumerate(r):
        if not c:  # black pixel
            moves.append(draw(x, y))
        # moves.append(goto(x,y))


# todo compression of nearby pixels?

print(moves)
moves_str = "\n  ".join(moves)

scheme = f'\
;;; Scheme Recursive Art Contest Entry\n\
;;;\n\
;;; Please do not include your name or personal info in this file.\n\
;;;\n\
;;; Title: M Scheme Eschqr\n\
;;;\n\
;;; Description:\n\
;;;   <strange loop emerging\n\
;;;    from a series of symbols\n\
;;;    that form another>\n\
\n\
(define (draw)\n\
  ; YOUR CODE HERE\n\
  (bgcolor "white")\n\
  {moves_str}\n\
  (ht)\n\
  (exitonclick))\n\
\n\
; Please leave this last line alone.  You may add additional procedures above\n\
; this line.\n\
(draw)\n'

print(scheme)
with open("contest.scm", "w") as fout:
    fout.write(scheme)
