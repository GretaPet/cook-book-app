from application import db
from application.models import Dishes

db.drop_all()
db.create_all()

testdish = Dishes(name='Fish & Chips')
db.session.add(testdish)
db.session.commit()