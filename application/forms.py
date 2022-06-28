from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, DecimalField, SelectField

class GameForm(FlaskForm):
    game_name = StringField("Game")
    genre = StringField("Genre")
    release_date = IntegerField("Date")
    price = DecimalField("Price")
    publisher = SelectField("Publisher")
    

class PublisherForm(FlaskForm):
    publisher_name = StringField("Publisher")
    submit = SubmitField("Submit")