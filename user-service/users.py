from src.utils.json_encoder import JSONEncoder
from src.mongo_handler import MongoHandler
from flask import Flask, jsonify, request, make_response
import requests
import os
import json

app = Flask(__name__)

mongo_handler = MongoHandler()


@app.route("/", methods=['GET'])
def hello():
    ''' Greet the user '''

    return "User service is up and running"


@app.route('/users', methods=['GET', 'POST'])
def users():
    if request.method == 'POST':
        payload = request.get_json(force=True, silent=True)
        return process_users_post(payload)

    if request.method == 'GET':
        return process_users_get()


@app.route('/users/<username>', methods=['GET'])
def user(username):
    ''' Returns info about a specific user '''
    return process_user_get(username)


@app.route('/users/<username>/talk/<talk_id>', methods=['POST'])
def user_talk(username, talk_id):
    ''' Reference user to talk '''

    talk = get_talk(talk_id)
    print(f'talk: {talk}')
    return mongo_handler.map_user_to_talk(username, talk)


def get_talk(talk_id):
    try:
        req = requests.get("http://127.0.0.1:5001/talk/{}".format(talk_id))
    except requests.exceptions.ConnectionError:
        return "Service talk unavailable"
    return req.text


def process_users_post(payload):
    ''' Save user into database and return user id '''

    inserted_id = mongo_handler.persist_user(payload)
    return json.dumps(inserted_id, cls=JSONEncoder)


def process_users_get():
    ''' Return all users from database '''

    users = mongo_handler.get_users()
    json_users = json.dumps(users, cls=JSONEncoder)
    return json_users


def process_user_get(id):
    ''' Return user from database '''

    user = mongo_handler.get_user(id)
    return json.dumps(user, cls=JSONEncoder)


if __name__ == '__main__':
    app.run(port=5000, debug=True)
