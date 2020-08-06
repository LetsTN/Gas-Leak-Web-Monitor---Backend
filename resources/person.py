from flask import Response, request
from flask_restful import Resource
from database.models import Persons

class PersonsApi(Resource):
  def get(self):
    # Retorna uma lista com todas as pessoas com o wearable
    persons = Persons.objects().to_json()
    return Response(persons, mimetype="application/json", status=200)

  def post(self):
    # Adiciona uma pessoa ao db
    body = request.get_json()
    person = Persons(**body).save()
    rasp_id = person.rasp_id
    return {'rasp_id': str(rasp_id)}, 200
 
class PersonApi(Resource):
  def put(self, id):
    # Edita as informações da pessoa com o id passado
    body = request.get_json()
    Persons.objects.get(rasp_id=id).update(**body)
    return '', 200
 
  def delete(self, id):
    # Deleta do db a pessoa com o id passado
    person = Persons.objects.get(rasp_id=id).delete()
    return '', 200

  def get(self, id):
    # Retorna as informações da pessoa com o id passado
    persons = Persons.objects.get(rasp_id=id).to_json()
    return Response(persons, mimetype="application/json", status=200)