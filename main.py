
from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

estado_actual = {"temperatura": None, "humedad": None, "ventilador": None, "confianza": None}

class SensorData(BaseModel):
    temperatura: float
    humedad: float

@app.get("/")
async def home():
    return FileResponse("static/index.html")

@app.post("/datos")
async def recibir_datos(data: SensorData):
    ventilador = "encender" if data.temperatura > 28 and data.humedad > 60 else "apagar"
    estado_actual.update({
        "temperatura": data.temperatura,
        "humedad": data.humedad,
        "ventilador": ventilador,
        "confianza": 0.95
    })
    return {"ventilador": ventilador}

@app.get("/estado")
async def obtener_estado():
    return estado_actual

@app.post("/reentrenar")
async def reentrenar():
    return {"mensaje": "Modelo reentrenado (simulado)"}

@app.get("/exportar")
async def exportar():
    return {"mensaje": "Datos exportados (simulado)"}
