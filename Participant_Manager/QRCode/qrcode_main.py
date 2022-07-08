import qrcode
from PIL import Image


class QRCode():
    def __init__(self, data):
        self.qrcode_text = data['name'] + '\n' + data['info'] + '\n id=' + data['id']
        self.qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        basewidth = 100
        self.logo = symposium_img()
        wpercent = (basewidth/float(self.logo.size[0]))
        hsize = int((float(self.logo.size[1])*float(wpercent)))
        self.logo = self.logo.resize((basewidth, hsize), Image.ANTIALIAS)
        self.make_image()

    def make_image(self):
        self.qr.add_data(self.qrcode_text)
        self.qr.make(fit=True)
        img = self.qr.make_image(fill_color="black", back_color="white")
        img.show()
        img.close()
        # save the QR code generated


def symposium_img():
    logo = Image.open("assets/images/logo_symp.png")
    return logo

if __name__ == "__main__":
    data = {'name':'MohammadAmin Alamalhoda', 'info':'1 lunch', 'id':'123456789'}
    qr_code_instance = QRCode(data)