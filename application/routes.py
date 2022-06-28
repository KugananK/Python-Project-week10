from application import app, db
from application.models import Games, Publishers
from application.forms import GameForm, PublisherForm
from flask import redirect, url_for, render_template, request

@app.route('/')
@app.route('/home')
@app.route('/indexgames')
def indexgames():
    game = Games.query.all()
    return render_template("game.html", Games = game)

@app.route('/about')
def about():
    return render_template('about.html')

@approute('/indexpublisher')
def indexpublisher:
    publisher = Publishers.query.all()
    return render_template("publisher.html", Publishers = publisher)

@app.route('/addgame', methods=['GET','POST'])
def addgame():
    form = GameForm()
    form.publisher.pubList = [(publishers.id,publishers.publisher_name) for publishers in Publishers.query.all()]
    if request.method == 'POST':
        if form.validate_on_submit():
            gameData = Games(
                game_name = form.game_name.data,
                genre = form.genre.data
                release_date = form.release_date.data
                price = form.price.data
                publisher_ID = form.publisher.data

            )
            db.session.add(gameData)
            db.session.commit()
        return redirect(url_for('home'))
    return render_template('addgame.html', form=form)

@app.route('/addpublisher', methods=['GET', 'POST'])
def addpublisher():
    form = PublisherForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            publisherData = Publisher(
                publisher_name = form.publisher_name.data
            )
            db.session.add(publisherData)
            db.session.commit()
        return redirect(url_for('indexpublisher'))
    return render_template('addpublisher.html', form=form)

