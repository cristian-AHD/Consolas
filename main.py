from fastapi import FastAPI

app = FastAPI()

# Ruta principal
@app.get("/")
def inicio():
    return {"mensaje": "consolas portátiles funcionando"}
