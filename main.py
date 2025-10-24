import json
from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")

estado_file = "estado.json"

class SensorData(BaseModel):
    temperatura: float
    humedad: float

@app.get("/")
async def home():
    return FileResponse("static/index.html")

@app.post("/datos")
async def recibir_datos(data: SensorData):
    ventilador = "encender" if data.temperatura > 28 and data.humedad > 60 else "apagar"
    estado_actual = {
        "temperatura": data.temperatura,
        "humedad": data.humedad,
        "ventilador": ventilador,
        "confianza": 0.95
    }
    with open(estado_file, "w") as f:
        json.dump(estado_actual, f)
    return {"ventilador": ventilador}

@app.get("/estado")
async def obtener_estado():
    try:
        with open(estado_file, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return {"temperatura": None, "humedad": None, "ventilador": None, "confianza": None}
