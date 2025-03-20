from flask import Flask, request, jsonify
from flask_restful import Api, Resource
from flask_cors import CORS
from pymongo import MongoClient
from bson.objectid import ObjectId

import bcrypt
import os

app = Flask(__name__)
api = Api(app)
CORS(app)

# MongoDB setup
client = MongoClient("mongodb://localhost:27017/")
db = client["to-do"]
users = db["users"]
tasks_collection = db["tasks"]

class Signup(Resource):
    def post(self):
        data = request.get_json()
        username = data.get("username")
        email = data.get("email")
        password = data.get("password")

        if users.find_one({"email": email}):
            return jsonify({"message": "Email already exists", "status": "error"})

        hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
        users.insert_one({"username": username, "email": email, "password": hashed_password})

        return jsonify({"message": "Signup successful", "status": "success"})

class Login(Resource):
    def post(self):
        data = request.get_json()
        email = data.get("email")
        password = data.get("password")

        user = users.find_one({"email": email})
        if not user or not bcrypt.checkpw(password.encode('utf-8'), user["password"]):
            return jsonify({"message": "Invalid email or password", "status": "error"})

        return jsonify({"message": "Login successful", "status": "success"})

api.add_resource(Signup, "/signup")
api.add_resource(Login, "/login")

@app.route('/tasks', methods=['GET'])
def get_tasks():
    tasks = []
    for task in tasks_collection.find():
        tasks.append({
            'id': str(task['_id']),
            'title': task['title'],
            'description': task['description'],
            'status': task['status']
        })
    return jsonify(tasks)

@app.route('/tasks', methods=['POST'])
def add_task():
    data = request.json
    task_id = tasks_collection.insert_one({
        'title': data['title'],
        'description': data['description'],
        'status': data['status']
    }).inserted_id
    return jsonify({'id': str(task_id)})

@app.route('/tasks/<task_id>', methods=['PUT'])
def update_task(task_id):
    data = request.json
    tasks_collection.update_one({'_id': ObjectId(task_id)}, {'$set': {
        'title': data['title'],
        'description': data['description'],
        'status': data['status']
    }})
    return jsonify({'message': 'Task updated successfully'})

@app.route('/tasks/<task_id>', methods=['DELETE'])
def delete_task(task_id):
    tasks_collection.delete_one({'_id': ObjectId(task_id)})
    return jsonify({'message': 'Task deleted successfully'})

if __name__ == "__main__":
    app.run(debug=True)
