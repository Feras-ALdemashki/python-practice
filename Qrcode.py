import qrcode

data = input("enter URL: ").strip()

qr = qrcode.QRCode()
qr.add_data(data)
qr.make()
qr.print_ascii(invert=True)