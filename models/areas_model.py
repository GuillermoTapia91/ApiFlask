from sqlalchemy.schema import Column
from sqlalchemy import types
from base_de_datos import conexion


class AreaModel(conexion.Model):
    id = Column(type_=types.Integer, autoincrement=True, primary_key=True)
    nombre = Column(type_=types.Text, nullable=False, unique=True)
    piso = Column(type_=types.Integer, nullable=False)

    __tablename__ = 'areas'
