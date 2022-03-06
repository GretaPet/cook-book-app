from application import app, db
from application.models import Dishes
from flask import render_template

@app.route('/create/<name>', methods=['GET'])
def create(name):
    dish = Dishes(name=name, description="A new dish")
    db.session.add(dish)
    db.session.commit()
    return render_template('create.html', name=name)

@app.route('/read', methods=['GET'])
def read():
    dishes = Dishes.query.all()
    return render_template('read.html', dishes=dishes)


@app.route('/update/<newname>', methods=['GET'])
def update(newname):
    dish = Dishes.query.first()
    old_name = dish.name
    dish.name = newname
    db.session.commit()
    return render_template('update.html', oldname=old_name, newname=newname)

@app.route('/delete/<name>', methods=['GET'])
def delete(name):
    dish = Dishes.query.filter_by(name=name).first()
    old_name = dish.name
    db.session.delete(dish)
    db.session.commit()
    return render_template('delete.html', oldname=old_name)

@app.route('/complete/<name>', methods=['GET'])
def complete(name):
    dish = Dishes.query.filter_by(name=name).first()
    tasks = Dishes.query.all()
    error = ""
    if dish:
        dish.completed = True
        db.session.commit()
    else:
        error = f'No dish with that name could be found in the database, please try again.'
    return render_template('tasks.html', error=error, tasks=tasks)

@app.route('/incomplete/<name>', methods=['GET'])
def incomplete(name):
    dish = Dishes.query.filter_by(name=name).first()
    tasks = Dishes.query.all()
    error = ""
    if dish:
        dish.completed = False
        db.session.commit()
    else:
        error = f'No dish with that name could be found in the database, please try again.'
    return render_template('tasks.html', error=error, tasks=tasks)