from flask_restful import Resource, request
from base_de_datos import conexion
from models.areas_model import AreaModel
from dtos.area_dto import AreaResponseDto, AreaRequestDto


class AreasController(Resource):
    def get(self):
        resultado = conexion.session.query(AreaModel).all()
        dto = AreaResponseDto(many=True)
        # convertir la data a un diccionario con dump
        data = dto.dump(resultado)

        return {
            'content': data
        }

    def post(self):
        data = request.json
        dto = AreaRequestDto()
        dataValidada = dto.load(data)
        print(dataValidada)
        # inicializo mi nuevo usuario

        nuevaArea = AreaModel(**dataValidada)
        conexion.session.add(nuevaArea)
        try:
            conexion.session.commit()
            return {
                'message': 'Area creada exitosamente'
            }, 201
        except Exception as error:
            conexion.session.rollback()
            return {
                'message': 'Soy un error',
                'content': error.args
            }, 400
