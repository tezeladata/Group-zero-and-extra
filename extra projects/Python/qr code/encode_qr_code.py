import qrcode

data = input("Enter text you want qr code to be generated for: ")

# Design
qr = qrcode.QRCode(version = 1, box_size = 10, border = 5)
qr.add_data(data)

qr.make(fit=True)

img = qr.make_image(fill_color = "grey", back_color = "black")

img.save(f"./qr code/{data}.png")