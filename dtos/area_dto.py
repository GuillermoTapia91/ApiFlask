from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from models.areas_model import AreaModel


class AreaResponseDto(SQLAlchemyAutoSchema):
    class Meta:
        model = AreaModel


class AreaRequestDto(SQLAlchemyAutoSchema):
    class Meta:
        model = AreaModel
