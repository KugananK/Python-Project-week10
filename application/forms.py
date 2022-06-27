from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, DecimalField

class GameForm(FlaskForm):
    game_name = StringField("Game")
    genre = StringField("Genre")
    release_date = IntegerField("Date")
    price = DecimalField("Price")
    publisher = StringField("Publisher")
    

class PublisherForm(FlaskForm):
    publisher_name = StringField("Publisher")
    submit = SubmitField("Submit")