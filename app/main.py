from typing import Union

from fastapi import FastAPI
from app.server import SystemConfig
app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "world is nothign"}


@app.get("/system")
def read_system_config():
    return SystemConfig.get_system_info()
