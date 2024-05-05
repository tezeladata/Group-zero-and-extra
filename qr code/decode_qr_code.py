from pyzbar.pyzbar import decode
from PIL import Image

img = Image.open("./qr code/test1.png")

result = decode(img)

print(result)