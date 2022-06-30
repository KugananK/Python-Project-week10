from application import db
from application.models import Games, Publishers

db.drop_all()
db.create_all()

sample_publisher = Publishers(
    publisher_name = "Sample publisher",
)
db.session.add(sample_publisher)
db.session.commit()