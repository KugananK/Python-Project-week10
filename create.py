from application import db
from application.models import Games, Publishers

db.drop_all()
db.create_all()