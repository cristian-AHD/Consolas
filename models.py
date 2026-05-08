from sqlalchemy import Column, Integer, String, Float
from database import Base

class Consola(Base):
    __tablename__ = "consolas_portatiles"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String)
    anio_salida = Column(Integer)
    precio_salida = Column(Float)


class Juego(Base):
    __tablename__ = "juegos"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String)
    precio = Column(Float)
    rating = Column(Float)
