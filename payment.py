import qrcode


def get_payment_img_path(debt): 
    url=f"paypal.me/coffeeataibe/{debt:.2f}"
        # Generate QR code
    qr = qrcode.QRCode(
        version=1,  # controls the size of the QR Code; 1 is the smallest, and it increases to hold more data
        error_correction=qrcode.constants.ERROR_CORRECT_L,  # controls the error correction used for the QR Code
        box_size=10,  # controls how many pixels each “box” of the QR code is
        border=4,  # controls how many boxes thick the border should be
    )
    qr.add_data(url)
    qr.make(fit=True)

    # Create an image from the QR Code instance
    img = qr.make_image(fill_color="black", back_color="white")

    # Save the image to a file
    path = "payment_tmp.png"
    img.save(path)
    return path 
