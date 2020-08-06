from flask import Flask
from database.db import initialize_db
from flask_restful import Api

from resources.routes import initialize_routes

app = Flask(__name__)
api = Api(app)

app.config['MONGODB_SETTINGS'] = {
    'host': 'mongodb://admin:admin@cluster0-shard-00-00.mcpl9.mongodb.net:27017,cluster0-shard-00-01.mcpl9.mongodb.net:27017,cluster0-shard-00-02.mcpl9.mongodb.net:27017/wam?ssl=true&replicaSet=atlas-92jwdx-shard-0&authSource=admin&retryWrites=true&w=majority'
}

initialize_db(app)
initialize_routes(api)

app.run()