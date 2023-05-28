from flask_restful import Resource, request
from base_de_datos import conexion
from models.empleados_model import EmpleadoModel
from dtos.empleado_dto import EmpleadoResponseDto, EmpleadoRequestDto


class EmpleadosController(Resource):
    def get(self):
        resultado = conexion.session.query(EmpleadoModel).all()
        dto = EmpleadoResponseDto(many=True)
        # convertir la data a un diccionario con dump
        data = dto.dump(resultado)

        return {
            'content': data
        }

    def post(self):
        data = request.json
        dto = EmpleadoRequestDto()
        dataValidada = dto.load(data)
        print(dataValidada)
        # inicializo mi nuevo usuario

        nuevoEmpleado = EmpleadoModel(**dataValidada)
        conexion.session.add(nuevoEmpleado)
        try:
            conexion.session.commit()
            return {
                'message': 'Empleado creado exitosamente'
            }, 201
        except Exception as error:
            conexion.session.rollback()
            return {
                'message': 'Hay un error',
                'content': error.args
            }, 400
