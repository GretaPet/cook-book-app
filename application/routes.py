from application import app, db
from application.models import Dishes
from flask import render_template

@app.route('/')
def cook_book():
    return "CookBook WebApp"

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/create/<name>', methods=['GET'])
def create(name):
    dish = Dishes(name=name)
    db.session.add(dish)
    db.session.commit()
    return f'Added new dish: {name}'

@app.route('/read', methods=['GET'])
def read():
    dishes = Dishes.query.all()
    return_string = ""
    for dish in dishes:
        return_string += str(dish.name) + '<br>'
    if return_string == "":
        return f'There are no dishes in the database'
    else:
        return f'{return_string}'

@app.route('/update/<newname>', methods=['GET'])
def update(newname):
    dish = Dishes.query.first()
    old_name = dish.name
    dish.name = newname
    db.session.commit()
    return f'The dish with name: {old_name}, has been renamed to {newname}'

@app.route('/delete/<name>', methods=['GET'])
def delete(name):
    dish = Dishes.query.filter_by(name=name).first()
    name = dish.name
    db.session.delete(dish)
    db.session.commit()
    return f'The dish with name: {name}, has been deleted'
