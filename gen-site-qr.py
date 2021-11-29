import qrcode
import sys
from PIL import Image

FNAME = "url-qr.png"


qr = qrcode.QRCode(
    border=1, version=1, error_correction=qrcode.constants.ERROR_CORRECT_L
)
qr.add_data(open("CNAME").read())
img = qr.make_image(fit=True)
img.save(FNAME)

# since bits aren't 1:1 with pixels (they're 1:4), this is hard
# stdoutOrigin = sys.stdout
# sys.stdout = open("url-qr.txt", "w")
# qr.print_ascii()

# resizing is easier
file = Image.open(FNAME)
file = file.resize((23, 23), Image.NEAREST)
file.save(FNAME)
