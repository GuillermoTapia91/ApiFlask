from flask import Flask
from base_de_datos import conexion
from flask_migrate import Migrate
from flask_restful import Api
from models.areas_model import AreaModel
from models.empleados_model import EmpleadoModel
from controllers.area_controller import AreasController
from controllers.empleado_controller import EmpleadosController
from controllers.area_unitaria_controller import AreaUnitariaController

app = Flask(__name__)

# Sirve para agregar la librería flask_resrful a nuestro proyecto flask
api = Api(app=app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:password@localhost:5432/empresas'

conexion.init_app(app)

Migrate(app, conexion)

api.add_resource(AreasController, '/areas', '/area')
api.add_resource(AreaUnitariaController, '/area/<int:id>')
api.add_resource(EmpleadosController, '/empleado', '/empleados')

if __name__ == '__main__':
    app.run(debug=True)
