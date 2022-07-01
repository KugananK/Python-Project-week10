from application import app, db
from flask_testing import TestCase
from application.models import Games, Publishers
from application.forms import GameForm, PublisherForm
from flask import redirect, url_for, render_template, request

class TestBase(TestCase):
    def create_app(self):
        app.config.update(SQLALCHEMY_DATABASE_URI="sqlite:///testdata.db",
                SECRET_KEY='TEST_SECRET_KEY',
                DEBUG=True,
                WTF_CSRF_ENABLED=False
                )
        return app

    def setUp(self):
        db.create_all()

        testPublisher = Publishers(
            publisher_name = "SampleTestPublisher"
        )
        db.session.add(testPublisher)
        db.session.commit()

        testGame = Games(
            game_name = "SampleTestGame",
            genre = "RPG",
            release_date = 2017,
            price = 9.99,
            publisher_ID = 1
        )
        db.session.add(testGame)
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

class TestViews(TestBase):
    def test_game_get(self):
        response = self.client.get(url_for('indexgames'))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'SampleTestGame', response.data)

    def test_publisher_get(self):
        response = self.client.get(url_for('indexpublishers'))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'SampleTestPublisher', response.data)

class TestCreateGame(TestBase):
    def test_create_game(self):
        response = self.client.post(
            url_for('addgame'),
            data = dict(game_name = "SampleTestGame2",
            genre = "RPG",
            release_date = 2017,
            price = 9.99,
            publisher_ID = 1
            )
        )
        assert Games.query.filter_by(game_name="SampleTestGame2").first().id == 2

    def test_addgame_get(self):
        response = self.client.get(url_for('addgame'))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Game Name', response.data)

class TestCreatePublisher(TestBase):
    def test_create_publisher(self):
        response = self.client.post(
            url_for('addpublisher'),
            data = dict(publisher_name="SampleTestPublisher2"
            )
        )
        assert Publishers.query.filter_by(publisher_name="SampleTestPublisher2").first().id == 2

    def test_addpublisher_get(self):
        response = self.client.get(url_for('addpublisher'))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Publisher Name', response.data)

class TestDeleteGame(TestBase):
    def test_delete_game(self):
        response = self.client.get(url_for('deletegame', id = 1))
        assert len(Games.query.all()) == 0

class TestDeletePublisher(TestBase):
    def test_delete_publisher(self):
        response = self.client.get(url_for('deletepublisher', id = 1))
        assert len(Publishers.query.all()) == 0

class TestUpdateGame(TestBase):
    def test_updategame_post(self):
        response = self.client.post(
            url_for('updategame', id = 1),
            data = dict(
            game_name = "SampleTestGame2",
            genre = "RPG",
            release_date = 2017,
            price = 9.99,
            publisher_ID = 1
            )
        )
    assert Games.query.filter_by(game_name="SampleTestGame2")

    def test_updategame_get(self):
        response = self.client.get(url_for('updategame', id=1))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Update Game', response.data)

class TestUpdatePublisher(TestBase):
    def test_updatepublisher_post(self):
        response = self.client.post(
            url_for('updatepublisher', id=1),
            data = dict(
            publisher_name="SampleTestPublisher2"
            )
        )
        assert Publisher.query.filter_by(publisher_name="SampleTestPublisher2")