from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# SQL Server Configuration (Update your details)
app.config["SQLALCHEMY_DATABASE_URI"] = "mssql+pyodbc://hsavaj:pass%40word1@harshilssqlserver.database.windows.net/SampleDB?driver=ODBC+Driver+17+for+SQL+Server"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

# Database Model
class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    task = db.Column(db.String(200), nullable=False)
    completed = db.Column(db.Boolean, default=False)

# Create Database Tables
with app.app_context():
    db.create_all()

@app.route("/")
def home():
    return "Welcome to Flask To-Do API!"

@app.route("/todos", methods=["GET"])
def get_todos():
    todos = Todo.query.all()
    return jsonify([{"id": t.id, "task": t.task, "completed": t.completed} for t in todos])

@app.route("/todos", methods=["POST"])
def add_todo():
    data = request.json
    new_todo = Todo(task=data["task"])
    db.session.add(new_todo)
    db.session.commit()
    return jsonify({"message": "Task added!"}), 201

@app.route("/todos/<int:id>", methods=["PUT"])
def update_todo(id):
    todo = Todo.query.get(id)
    if not todo:
        return jsonify({"message": "Task not found"}), 404
    todo.completed = True
    db.session.commit()
    return jsonify({"message": "Task completed!"})

@app.route("/todos/<int:id>", methods=["DELETE"])
def delete_todo(id):
    todo = Todo.query.get(id)
    if not todo:
        return jsonify({"message": "Task not found"}), 404
    db.session.delete(todo)
    db.session.commit()
    return jsonify({"message": "Task deleted!"})

if __name__ == "__main__":
    app.run(debug=True)
