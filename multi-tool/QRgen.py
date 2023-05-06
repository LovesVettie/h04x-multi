import qrcode

data = input("H04X QRgen/Bir Değer Gir: ")
img = qrcode.make(data)
img.save("QRgen-sonuc.png")
img.show()