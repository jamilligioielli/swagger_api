from flask_restplus import fields
from service.restplus import api

INPUT_MAIN_SERVICE = api.model(
  'input_main_service', {
    'a': fields.List(fields.Float(), required=True, description= "Valor numerico da variavel com grau 2"),
    'b': fields.List(fields.Float(), required=True, description= "Valor númerico da variavel de grau 1"),
    'c': fields.List(fields.Float(), required=True, description= "Valor númerico que restar")})
