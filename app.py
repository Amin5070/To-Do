from flask import Flask, request, jsonify
from flask_pymongo import PyMongo
from bson import ObjectId

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/MyDatabase"
mongo = PyMongo(app)


@app.route("/")
def hello():
    return "Welcome to the To-Do List API!"


@app.route("/tasks", methods=["POST"])
def add_task():
    data = request.get_json()
    task_id = mongo.db.tasks.insert_one(data).inserted_id
    return str(task_id), 201


@app.route("/tasks", methods=["GET"])
def get_tasks():
    tasks = list(mongo.db.tasks.find())
    for task in tasks:
        task["_id"] = str(task["_id"])
    return jsonify(tasks), 200


@app.route("/tasks/<string:task_id>", methods=["PUT"])
def update_task(task_id):
    data = request.get_json()
    result = mongo.db.tasks.update_one({"_id": ObjectId(task_id)}, {"$set": data})
    if result.modified_count == 1:
        return "Task updated successfully", 200
    else:
        return "Task not found or could not be updated", 404


@app.route("/tasks/<string:task_id>", methods=["DELETE"])
def delete_task(task_id):
    result = mongo.db.tasks.delete_one({"_id": ObjectId(task_id)})
    if result.deleted_count == 1:
        return "Task deleted successfully", 200
    else:
        return "Task not found or could not be deleted", 404


if __name__ == "__main__":
    app.run(debug=True, port=2100)
