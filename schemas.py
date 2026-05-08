from pydantic import BaseModel

# Consolas
class ConsolaBase(BaseModel):
    nombre: str
    anio_salida: int
    precio_salida: float

class ConsolaCreate(ConsolaBase):
    pass

# Juegos
class JuegoBase(BaseModel):
    nombre: str
    precio: float
    rating: float

class JuegoCreate(JuegoBase):
    pass