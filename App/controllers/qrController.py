from App.services import qrServices
from fastapi import APIRouter, Response
from fastapi.responses import Response
from pydantic import BaseModel
from qrcode.image.svg import SvgImage
from PIL import Image


# Modelo de datos de un codigo qr:
class QrData(BaseModel):
    data: str

# contexto
router = APIRouter(prefix="/qrgenerator", tags=["qrgenerator"])

# peticiones
@router.post("/svg")
async def qr_response(data: QrData):
    qr = qrServices.qr_generator(data.data)
    img_qr = qrServices.qr_to_svg(qr)
    img_qr_str = qrServices.svg_to_str(img_qr)
    return Response(content= img_qr_str, media_type="image/svg+xml")

@router.post("/png")
async def qr_response(data: QrData):
    qr = qrServices.qr_generator(data.data)
    img_qr = qrServices.qr_to_image(qr)
    img_qr_bytes = qrServices.image_to_byte(img_qr)
    return Response(content= img_qr_bytes, media_type="image/png")

