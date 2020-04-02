from src.utils.json_encoder import JSONEncoder
from src.mongo_handler import MongoHandler
from flask import Flask, jsonify, request, make_response
import requests
import os
import json

app = Flask(__name__)

database_path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
print(database_path)

with open("{}/database/users.json".format(database_path), "r") as f:
    usr = json.load(f)

mongo_handler = MongoHandler()

@app.route("/", methods=['GET'])
def hello():
    ''' Greet the user '''

    return "User service is up and running"

@app.route('/users', methods=['GET', 'POST'])
def users():
    if request.method == 'POST':
        payload = request.get_json(force=True, silent=True)
        print(f'/users: {request.method}, {payload}')
        return process_users_post(payload)

    if request.method == 'GET':
        print(f'/users: {request.method}')
        return process_users_get()

@app.route('/users/<id>', methods=['GET'])
def user(id):
    ''' Returns info about a specific user '''
    return process_user_get(id)

@app.route('/users/<username>/lists', methods=['GET'])
def user_lists(username):
    ''' Get lists based on username '''

    try:
        req = requests.get("http://127.0.0.1:5001/lists/{}".format(username))
    except requests.exceptions.ConnectionError:
        return "Service unavailable"
    return req.text

def process_users_post(payload):
    ''' Save user into database and return user id '''

    inserted_id = mongo_handler.persist_user(payload)
    print(f'process_users_post: {inserted_id}')
    return json.dumps(inserted_id, cls=JSONEncoder)

def process_users_get():
    ''' Return all users from database '''

    users = mongo_handler.get_users()
    json_users = json.dumps(users, cls=JSONEncoder)
    print(f'process_users_get: {json_users}')
    return json_users

def process_user_get(id):
    ''' Return user from database '''

    users = mongo_handler.get_user(id)
    json_users = json.dumps(users, cls=JSONEncoder)
    print(f'process_users_get: {json_users}')
    return json_users

if __name__ == '__main__':
    app.run(port=5000, debug=True)
