from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), unique=False, nullable=False)
    completed = db.Column(db.Boolean, default=False)


@app.route('/')
def index():
    #show all todos
    todo_list = Todo.query.all()
    return render_template('base.html', todo_list=todo_list)

@app.route("/add", methods=["POST"])
def add():
    #add new item
    #add a new todo item to the database
    title = request.form.get("title")
    new_todo = Todo(title=title, completed=False)
    db.session.add(new_todo)
    db.session.commit()
    return redirect(url_for('index'))


@app.route("/update/<int:todo_id>")
def update(todo_id):
    todo = Todo.query.filter_by(id=todo_id).first()
    todo.completed = not todo.completed
    db.session.commit()
    return redirect(url_for('index'))

@app.route("/delete/<int:todo_id>")
def delete(todo_id):
    todo = Todo.query.filter_by(id=todo_id).first()
    db.session.delete(todo)
    db.session.commit()
    return redirect(url_for('index'))



if __name__ == '__main__':

    # create the application context
    with app.app_context():
        db.create_all() 
    #run the Flask application
    app.run(debug=True)