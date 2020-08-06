from flask import Response, request
from flask_restful import Resource
from database.models import Rasps

class RaspsApi(Resource):
  def get(self):
    # Retorna uma lista com todas as modulos com o wearable
    rasps = Rasps.objects().to_json()
    return Response(rasps, mimetype="application/json", status=200)

  def post(self):
    # Adiciona uma modulo ao db
    body = request.get_json()
    print(body)

    ## Verifica se a id da rasp já existe
    rasp_id = body['rasp_id']
    #rasps = Rasps.objects().to_json()
    #match = [i for i in rasps if i['rasp_id']==rasp_id]
    #print(rasp_id, rasps, match)

    ## Se existir retorna um erro
    #if len(match) == 0:
      #return {'error': 'ID already exists'}, 409

    ## Se n, adiciona o modulo ao db 
    #new_rasp = Rasps(**body).save()
    return {'rasp_id': str(rasp_id)}, 200
 
class RaspApi(Resource):
  def put(self, id):
    # Edita as informações da modulo com o id passado 
    body = request.get_json()
    Rasps.objects.get(rasp_id=id).update(**body)
    return '', 200
 
  def delete(self, id):
    # Deleta do db a modulo com o id passado
    rasp = Rasps.objects.get(rasp_id=id).delete() 
    return '', 200

  def get(self, id):
    # Retorna as informações da modulo com o id passado
    rasps = Rasps.objects.get(rasp_id=id).to_json()
    return Response(rasps, mimetype="application/json", status=200)