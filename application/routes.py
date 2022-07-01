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

@app.route('/indexpublishers')
def indexpublishers():
    publisher = Publishers.query.all()
    return render_template("publisher.html", Publishers = publisher)

@app.route('/addgame', methods=['GET','POST'])
def addgame():
    form = GameForm()
    form.publisher.choices = [(publishers.id,publishers.publisher_name) for publishers in Publishers.query.all()]
    if request.method == 'POST':
        gameData = Games(
            game_name = form.game_name.data,
            genre = form.genre.data,
            release_date = form.release_date.data,
            price = form.price.data,
            publisher_ID = form.publisher.data
        )
        db.session.add(gameData)
        db.session.commit()
        return redirect(url_for('indexgames'))
    return render_template('addgame.html', form=form)

@app.route('/addpublisher', methods=['GET', 'POST'])
def addpublisher():
    form = PublisherForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            publisherData = Publishers(
                publisher_name = form.publisher_name.data
            )
            db.session.add(publisherData)
            db.session.commit()
            return redirect(url_for('indexpublishers'))
    return render_template('addpublisher.html', form=form)

@app.route('/deletegame/<int:id>')
def deletegame(id):
    game = Games.query.get(id)
    db.session.delete(game)
    db.session.commit()
    return redirect(url_for('indexgames'))

@app.route('/deletepublisher/<int:id>')
def deletepublisher(id):
    publisher = Publishers.query.get(id)
    db.session.delete(publisher)
    db.session.commit()
    return redirect(url_for('indexpublishers'))

@app.route('/updategame/<int:id>', methods= ['GET', 'POST'])
def updategame(id):
    form = GameForm()
    form.publisher.choices = [(publishers.id,publishers.publisher_name) for publishers in Publishers.query.all()]
    game = Games.query.get(id)
    if request.method == 'POST':
        game.game_name = form.game_name.data
        game.genre = form.genre.data
        game.release_date = form.release_date.data
        game.price = form.price.data
        game.publisher_ID = form.publisher.data
        db.session.commit()
        return redirect(url_for('indexgames'))
    elif request.method == 'GET':
        game.game_name = form.game_name.data
        game.genre = form.genre.data
        game.release_date = form.release_date.data
        game.price = form.price.data
        game.publisher = form.publisher.data
    return render_template('updategame.html', form=form)

@app.route('/updatepublisher/<int:id>', methods= ['GET', 'POST'])
def updatepublisher(id):
    form = PublisherForm()
    publisher = Publishers.query.get(id)
    if request.method == 'POST':
        if form.validate_on_submit():
            publisher.publisher_name = form.publisher_name.data
            db.session.commit()
            return redirect(url_for('indexpublishers'))
    return render_template('updatepublisher.html', form=form)

@app.route('/publishergames/<id>')
def publishergames(id):
    publishers = Publishers.query.get(id)
    gameList = []
    game = Games.query.all()
    for games in game:
        if games.publisher_ID == publishers.id:
            gameList.append(games.game_name)
    gameList = ", ".join(gameList)
    return render_template('publishergames.html', Publishers=publishers, Games=gameList)