# Import necessary libraries
import qrcode
from PIL import Image

# Create a QRCode object with specific parameters
qr = qrcode.QRCode(
    version=1,  # version controls the size of the QR code: 1 is the smallest (21x21)
    error_correction=qrcode.constants.ERROR_CORRECT_H,  # high error correction (up to 30%)
    box_size=20,  # size of each box in the QR code,attributes of QRCode class.
    border=4,  # thickness of the white border (in boxes)
)

# Add data to the QR code
qr.add_data("https://hbtu.ac.in/") #method from QRcode class

# Generate the QR code with automatic version adjustment if needed
# qr.make(fit=True)

# Create an image from the QR code with custom colors
img = qr.make_image(fill_color="red", back_color="white")

# Save the image to a file
img.save("hbtu_main_page.png")
