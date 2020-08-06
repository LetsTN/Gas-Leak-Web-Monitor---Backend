from .person import PersonsApi, PersonApi
from .reading import ReadingsApi, ReadingApi
from .rasp import RaspsApi, RaspApi

def initialize_routes(api):
	api.add_resource(PersonsApi, '/persons')
	api.add_resource(PersonApi, '/person/<id>')
	api.add_resource(ReadingsApi, '/readings')
	api.add_resource(ReadingApi, '/reading/<id>')
	api.add_resource(RaspsApi, '/rasps')
	api.add_resource(RaspApi, '/rasp/<id>')