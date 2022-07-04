from application import db
from application.models import Games, Publishers

db.drop_all()
db.create_all()

sample_publisher = Publishers(
    publisher_name = "Sample publisher",
)
db.session.add(sample_publisher)
db.session.commit()

sample_game = Games(
        game_name = "SampleTestGame2",
        genre = "RPG",
        release_date = 2017,
        price = 9.99,
        publisher_ID = 1
        )
db.session.add(sample_game)
db.session.commit()