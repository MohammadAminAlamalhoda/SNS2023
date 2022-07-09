import qrcode
from PIL import Image

class QRCode():
    def __init__(self):
        self.qr = qrcode.QRCode(
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )

    def make_image(self, user_info):
        qrcode_text = "Name= " + str(user_info[1]) + "\n Email= " + str(user_info[2]).replace('@', ' AT ').replace('.', ' DOT ') + "\n Lunchs= " + str(user_info[3]) + "\n Snacks= " + str(user_info[4]) + "\n SNS-ID= " + str(user_info[0])
        self.qr.clear()
        self.qr.add_data(qrcode_text)
        self.qr.make(fit=True)
        img = self.qr.make_image(fill_color="blue", back_color="white")
        return img
        
def symposium_img():
    logo = Image.open("QRCode/assets/images/logo_symp.png")
    return logo