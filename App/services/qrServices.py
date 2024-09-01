import qrcode #documentacion: https://github.com/lincolnloop/python-qrcode/tree/main
import qrcode.constants
import qrcode.image.svg
from qrcode.image.svg import SvgImage
from PIL import Image
from io import BytesIO


def qr_generator(data: str) -> qrcode.main.QRCode:
    qr = qrcode.QRCode(
        version=None,
        error_correction=qrcode.constants.ERROR_CORRECT_M,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)

    return qr


def qr_to_image(
    qr: qrcode.main.QRCode, fill_color: str = "black", back_color: str = "white"
) -> Image:
    img_qr = qr.make_image(fill_color=fill_color, back_color=back_color)
    return img_qr


def qr_to_svg(
    qr: qrcode.main.QRCode, fill_color: str = "black", back_color: str = "white"
) -> SvgImage:
    svg_qr = qr.make_image(
        image_factory=qrcode.image.svg.SvgImage,
        fill_color=fill_color,
        back_color=back_color,
    )
    return svg_qr


def svg_to_str(svg: SvgImage):
    return svg.to_string()

def image_to_byte(img: Image):
    byte_obj = BytesIO()
    img.save(byte_obj, format = "PNG")
    img_bytes = byte_obj.getvalue()
    return img_bytes
    
def save_svg(qr_svg: SvgImage, file_name: str = "qr.svg"):
    qr_svg.save(file_name)

def save_png(qr_png: Image, file_name: str = "qr.png"):
    qr_png.save(file_name)


# testing
execute = False
if __name__ == "__main__" and execute:
    qr = qr_generator("hola mundo")
    qr_svg = qr_to_svg(qr)
    # save_qr_png(qr_png)
    # save_qr_svg(qr_svg)
