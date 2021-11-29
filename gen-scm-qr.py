# generates QR encoding the scheme code from mse.mehvix.com that draws the QR code that ...

import qrcode

SCHEME_DATA = open("file.scm")
# comperession may be needed -- max of ~3k characters (?)
# later comment -- we don't need to worry bc we will encode the URL, not sceme code

qr = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_L)
qr.add_data(SCHEME_DATA)
img = qr.make_image()
img.save("scm-qr.png")
