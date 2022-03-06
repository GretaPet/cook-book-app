from application import db
from application.models import Dishes

db.drop_all()
db.create_all()