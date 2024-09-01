from fastapi import FastAPI
from App.controllers import qrController


app = FastAPI()
app.include_router(qrController.router)