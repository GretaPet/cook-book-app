from os import name
from flask import url_for
from flask_testing import TestCase
from application import app, db
from application.models import Dishes

class TestBase(TestCase):

    def create_app(self):
        app.config.update(
            SQLALCHEMY_DATABASE_URI='sqlite:///',
            DEBUG=True,
            WTF_CSRF_ENABLED=False)
        return app

    def setUp(self):

        db.session.commit()
        db.drop_all()
        db.create_all()

        dish1=Dishes(name='pizza')
        dish2=Dishes(name='pasta')

        db.session.add(dish1)
        db.session.add(dish2)
        db.session.commit()

    def tearDown(self):
        
        db.session.remove()
        db.drop_all()

class TestDishes(TestBase):

    def test_cookbook(self):
        response = self.client.get(url_for('cook_book'))
        self.assertEqual(response.status_code, 200)
        
    def test_read(self):
        response = self.client.get(url_for('read'))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'pizza', response.data)

    def test_home(self):
        response = self.client.get(url_for('home'))
        self.assertEqual(response.status_code, 200)
