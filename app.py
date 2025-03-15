from qrcode_styled import QRCodeStyled

from fastapi import FastAPI
from fastapi.responses import Response

app = FastAPI()


@app.get('/{data}')
async def get_qr_code(data: str):
    qr = QRCodeStyled(box_size=120)
    qrcode = qr.get_buffer(data=data, lossless=False, quality=100, method=2)

    return Response(content=qrcode.getvalue(), media_type='image/jpeg')
