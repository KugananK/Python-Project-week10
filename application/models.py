from application import db

class Games(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    game_name = db.Column(db.String(30))
    genre = db.Column(db.String(30))
    release_date = db.Column(db.Integer)
    price = db.Column(db.Decimal)
    publisher_ID = db.Column(db.Integer, db.ForeignKey(Publishers.id), nullable = False)
    publisher = db.relationship('Publishers', backref = 'publisher')

class Publishers(db.model):
    id = db.column(db.Integer,primary_key = True)
    publisher_name = db.column(db.String)