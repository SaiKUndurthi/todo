from flask import Flask, render_template, request, redirect, url_for, jsonify
from flask_sqlalchemy import SQLAlchemy
from env import dbstring
import sys

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']=dbstring #"postgres://user:password@localhost:5432/todoapp"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
db = SQLAlchemy(app)

class Todo(db.Model):
    __tablename__ = "todos"
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(), nullable=False)

    def __repr__(self):
        return f'<Todo {self.id} {self.description}>'

db.create_all()

# todo1 = Todo(description="Test entry to the database")
# db.session.add(todo1)
#
# Todo.query.first()
@app.route("/")
def index():
    return render_template("index.html", data=Todo.query.all())

@app.route("/todos/create",methods=['POST'])
def create_todo():
    error = False
    try:
        # todo_item = request.form.get('description','')
        todo_item = request.get_json()['description']
        print(todo_item)
        todo = Todo(description=todo_item)
        db.session.add(todo)
        db.session.commit()
    except:
        db.session.rollback()
        error = True
        print(sys.exc_info())
    finally:
        db.session.close()
    if not error:
        # return redirect(url_for('index'))
        return jsonify({
        'description': todo.description
        })
