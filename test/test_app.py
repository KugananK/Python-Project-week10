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
