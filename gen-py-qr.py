import qrcode

SCHEME_DATA = open("img-min.py").read()
# SCHEME_DATA = open("img-to-scm.py").read()

qr = qrcode.QRCode()
qr.add_data(SCHEME_DATA)
img = qr.make_image()
img.save("py-qr.png")
