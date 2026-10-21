from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def beranda():
    return {"status": "API aktif"}