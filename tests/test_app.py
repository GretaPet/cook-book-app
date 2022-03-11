from os import name
from flask import url_for
from flask_testing import TestCase
from application import app
from application.models import Dishes

class TestBase(TestCase):

    def create_app(self):
        app.config.update(
            SQLALCHEMY_DATABASE_URI='sqlite:///',
            DEBUG=True,
            WTF_CSRF_ENABLED=False)
        return app

class TestDishes(TestBase):

    def test_cookbook(self):
        response = self.client.get(url_for('cook_book'))
        self.assertEqual(response.status_code, 200)
        
    def test_read(self):
        response = self.client.get(url_for('read'))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'pizza', response.data)

