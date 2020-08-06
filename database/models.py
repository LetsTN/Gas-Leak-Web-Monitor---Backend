from .db import db
import datetime

class Persons(db.Document):
    name = db.StringField(required=True)
    gender = db.StringField(required=True)
    birth = db.DateTimeField(required=True)
    rasp_id =  db.StringField(required=True)

class Readings(db.Document):
	rasp_id =  db.StringField(required=True)
	time_stamp = db.DateTimeField(default=datetime.datetime.now())
	lpg = db.DecimalField(required=True)
	co = db.DecimalField(required=True)
	bpm = db.DecimalField(required=True)

class Rasps(db.Document):
	rasp_id = db.StringField(required=True, unique=True)
	person_assigned = db.BooleanField(default=False)
	has_reading = db.BooleanField(default=False)
