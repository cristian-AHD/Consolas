from fastapi import FastAPI, HTTPException
from database import SessionLocal, engine, Base
import models
import schemas

app = FastAPI()

Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# Crear consola
@app.post("/consolas")
def crear_consola(consola: schemas.ConsolaCreate):
    db = SessionLocal()

    nueva_consola = models.Consola(
        nombre=consola.nombre,
        anio_salida=consola.anio_salida,
        precio_salida=consola.precio_salida
    )

    db.add(nueva_consola)
    db.commit()
    db.refresh(nueva_consola)
    db.close()

    return nueva_consola

@app.get("/consolas")
def listar_consolas():
    db = SessionLocal()
    consolas = db.query(models.Consola).all()
    db.close()
    return consolas


@app.get("/consolas/{id}")
def obtener_consola(id: int):
    db = SessionLocal()
    consola = db.query(models.Consola).filter(models.Consola.id == id).first()
    db.close()

    if not consola:
        raise HTTPException(status_code=404, detail="Consola no encontrada")

    return consola


@app.put("/consolas/{id}")
def actualizar_consola(id: int, datos: schemas.ConsolaCreate):
    db = SessionLocal()
    consola = db.query(models.Consola).filter(models.Consola.id == id).first()

    if not consola:
        db.close()
        raise HTTPException(status_code=404, detail="Consola no encontrada")

    consola.nombre = datos.nombre
    consola.anio_salida = datos.anio_salida
    consola.precio_salida = datos.precio_salida

    db.commit()
    db.refresh(consola)
    db.close()

    return consola

@app.delete("/consolas/{id}")
def eliminar_consola(id: int):
    db = SessionLocal()
    consola = db.query(models.Consola).filter(models.Consola.id == id).first()

    if not consola:
        db.close()
        raise HTTPException(status_code=404, detail="Consola no encontrada")

    db.delete(consola)
    db.commit()
    db.close()

    return {"mensaje": "Consola eliminada correctamente"}

@app.post("/juegos")
def crear_juego(juego: schemas.JuegoCreate):
    db = SessionLocal()

    nuevo_juego = models.Juego(
        nombre=juego.nombre,
        precio=juego.precio,
        rating=juego.rating
    )

    db.add(nuevo_juego)
    db.commit()
    db.refresh(nuevo_juego)
    db.close()

    return nuevo_juego

@app.get("/juegos")
def listar_juegos():
    db = SessionLocal()
    juegos = db.query(models.Juego).all()
    db.close()
    return juegos

@app.get("/juegos/{id}")
def obtener_juego(id: int):
    db = SessionLocal()
    juego = db.query(models.Juego).filter(models.Juego.id == id).first()
    db.close()

    if not juego:
        raise HTTPException(status_code=404, detail="Juego no encontrado")

    return juego

@app.put("/juegos/{id}")
def actualizar_juego(id: int, datos: schemas.JuegoCreate):
    db = SessionLocal()
    juego = db.query(models.Juego).filter(models.Juego.id == id).first()

    if not juego:
        db.close()
        raise HTTPException(status_code=404, detail="Juego no encontrado")

    juego.nombre = datos.nombre
    juego.precio = datos.precio
    juego.rating = datos.rating

    db.commit()
    db.refresh(juego)
    db.close()

    return juego

@app.delete("/juegos/{id}")
def eliminar_juego(id: int):
    db = SessionLocal()
    juego = db.query(models.Juego).filter(models.Juego.id == id).first()

    if not juego:
        db.close()
        raise HTTPException(status_code=404, detail="Juego no encontrado")

    db.delete(juego)
    db.commit()
    db.close()

    return {"mensaje": "Juego eliminado correctamente"}