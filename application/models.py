from application import db

class Publishers(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    publisher_name = db.Column(db.String)
    publisher = db.relationship('Games', backref = 'game')

class Games(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    game_name = db.Column(db.String(30))
    genre = db.Column(db.String(30))
    release_date = db.Column(db.Integer)
    price = db.Column(db.Float)
    publisher_ID = db.Column(db.Integer, db.ForeignKey(Publishers.id), nullable = False)