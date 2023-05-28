from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from models.empleados_model import EmpleadoModel


class EmpleadoResponseDto(SQLAlchemyAutoSchema):
    class Meta:
        model = EmpleadoModel
        include_fk = True


class EmpleadoRequestDto(SQLAlchemyAutoSchema):
    class Meta:
        model = EmpleadoModel
        include_fk = True
