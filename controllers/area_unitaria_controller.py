from flask_restful import Resource
from base_de_datos import conexion
from models.areas_model import AreaModel
from dtos.area_dto import AreaResponseDto


class AreaUnitariaController(Resource):

    def get(self, id):
        area = conexion.session.query(AreaModel).filter_by(id=id).first()
        if area is None:
            return {
                'message': 'Esta area no existe'
            }
        dto = AreaResponseDto()
        resultado = dto.dump(area)
        # convertir la data a un diccionario con dump

        return {
            'content': resultado
        }

    # def get(self):
    #     resultado = conexion.session.query(AreaModel).all()
    #     dto = AreaResponseDto(many=True)
    #     # convertir la data a un diccionario con dump
    #     data = dto.dump(resultado)

    #     return {
    #         'content': data
    #     }
