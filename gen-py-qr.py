#!/usr/bin/python
import sys
import qrcode

py = sys.argv[1]
fn = "py-qr-reg.png" if "min" in py else "py-qr-min.png"
SCHEME_DATA = open(py).read()

qr = qrcode.QRCode(border=1, error_correction=qrcode.constants.ERROR_CORRECT_L)
qr.add_data(SCHEME_DATA)
img = qr.make_image()
img.save(fn)
