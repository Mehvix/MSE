# generates QR encoding the scheme code from mse.mehvix.com that draws the QR code that ...

from os import read
import qrcode
import requests

PROTOCOL = "http"
# URI = "127.0.0.1:5500"
URI = open("CNAME").read()
FILE = "file.scm"
URL = f"{PROTOCOL}://{URI}/{FILE}"
SCHEME_DATA = requests.get(URL).text
# comperession may be needed -- max of ~3k characters (?)

qr = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_L)
qr.add_data(SCHEME_DATA)
img = qr.make_image()
img.save("qr.png")
