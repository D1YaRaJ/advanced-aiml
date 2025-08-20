import qrcode
link=input("Enter link:")
qr=qrcode.make(link)
qr.show()
qr.save("qr.png")