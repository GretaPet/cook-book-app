from application import db

dish_ingr= db.Table('dish_ingr',
    db.Column('dishes_id', db.Integer, db.ForeignKey('dishes.id')),
    db.Column('ingreedient_id', db.Integer, db.ForeignKey('ingreedient.id'))
)

class Dishes(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)

class Ingreedient(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    recipe = db.relationship('Dishes', secondary=dish_ingr, backref='recipes')