import qrcode
from PIL import Image 

def create_qr_code(name, certificate_url):
    qr = qrcode.QRCode(  
        version=1,
        box_size=10,
        border=4,
    )

    qr.add_data(certificate_url)
    qr.make(fit=True)

    img = qr.make_image(fill="black", back_color="white")

    img.save(f"{name}.png")
    print(f"QR code for {name} generated successfully.")

if __name__ == "__main__":
    name = input("name is : ")
    data = input("data is : ")
    create_qr_code(name, data)
