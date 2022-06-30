from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, DecimalField, SelectField

class GameForm(FlaskForm):
    game_name = StringField("Game Name")
    genre = StringField("Genre")
    release_date = IntegerField("Release Date")
    price = DecimalField("Price on release")
    publisher = SelectField("Publisher", choices=[])
    submit = SubmitField("Submit")
    

class PublisherForm(FlaskForm):
    publisher_name = StringField("Publisher Name")
    submit = SubmitField("Submit")