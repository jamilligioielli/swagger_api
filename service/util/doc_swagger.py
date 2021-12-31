from flask_restplus import fields
from service.restplus import api

INPUT_MAIN_SERVICE = api.model(
  'input_main_service', {
    'a': fields.Integer(required=True, description= "Valor númerico da variavel de grau 1"),
    'b': fields.Integer(required=True, description= "Valor númerico da variavel de grau 1"),
    'c': fields.Integer(required=True, description= "Valor númerico da variavel de grau 1")})

    # fields(fields.Integer(), required=True, description= "Valor númerico da variavel de grau 1")
