#!/usr/bin/python
import sys
import qrcode

py = sys.argv[1]
if "min" in py:
    fn, qual = "py-qr-reg.png", qrcode.constants.ERROR_CORRECT_L
else:
    fn, qual = "py-qr-min.png", qrcode.constants.ERROR_CORRECT_Q

SCHEME_DATA = open(py).read()

qr = qrcode.QRCode(border=1, error_correction=qual)
qr.add_data(SCHEME_DATA)
img = qr.make_image()
img.save(fn)
