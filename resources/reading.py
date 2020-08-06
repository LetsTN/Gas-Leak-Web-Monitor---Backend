from flask import Response, request
from flask_restful import Resource
from database.models import Readings

class ReadingsApi(Resource):
  def get(self):
    # Retorna uma lista com todas as leituras com o wearable
    readings = Readings.objects().to_json()
    return Response(readings, mimetype="application/json", status=200)

  def post(self):
    # Adiciona uma leitura ao db
    body = request.get_json()
    reading = Readings(**body).save()
    rasp_id = reading.rasp_id
    return {'rasp_id': str(rasp_id)}, 200
 
class ReadingApi(Resource):
  def put(self, id):
    # Edita as informações da leitura com o id passado
    body = request.get_json()
    Readings.objects.get(id=rasp_id).update(**body)
    return '', 200
 
  def delete(self, id):
    # Deleta do db a leitura com o id passado
    reading = Readings.objects.get(rasp_id=id).delete()
    return '', 200

  def get(self, id):
    # Retorna as informações da leitura com o id passado
    readings = Readings.objects.get(rasp_id=id).to_json()
    return Response(readings, mimetype="application/json", status=200)