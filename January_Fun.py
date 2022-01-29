import qrcode
from PIL import Image

img = qrcode.make('https://bit.ly/35ANxOQ')
img.save('qrcode.jpg')
img.show()
