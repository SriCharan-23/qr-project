import qrcode  # inbuilt module in python


url = input("Enter any URL:").strip() # Taking input
file_path = "qrcode.png"   # path selection


qr = qrcode.QRCode() # object creation
qr.add_data(url)


img = qr.make_image()
img.save(file_path)


print("QR Code Generated Successfully!")
