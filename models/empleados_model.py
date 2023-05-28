from sqlalchemy.schema import Column, ForeignKey
from sqlalchemy import types
from base_de_datos import conexion


class EmpleadoModel(conexion.Model):
    id = Column(type_=types.Integer, autoincrement=True, primary_key=True)
    nombre = Column(type_=types.Text, nullable=False)
    apellido = Column(type_=types.Text, nullable=False)
    email = Column(type_=types.Text, unique=True, nullable=False)
    areaid = Column(ForeignKey(column='areas.id'),
                    type_=types.Integer, nullable=False, name='area_id')

    __tablename__ = 'empleados'
