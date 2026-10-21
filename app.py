from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="AI Prediksi Kelulusan")

class DataSiswa(BaseModel):
    nilai: float

@app.get("/")
def beranda():
    return {"status": "API aktif"}

@app.get("/health")
def health():
    return {"status": "healthy"}

@app.post("/predict")
def prediksi(data: DataSiswa):
    if not 0 <= data.nilai <= 100:
        return {"error": "Nilai harus 0 sampai 100"}

    hasil = "Lulus" if data.nilai >= 75 else "Belum Lulus"
    return {
        "nilai": data.nilai,
        "prediksi": hasil
    }
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def beranda():
    return {"status": "API aktif"}

@app.get("/health")
def health():
    return {"status": "healthy"}