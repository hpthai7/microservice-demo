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
    ''' Greet the talk '''

    return "Talk service is up and running"

@app.route('/talks', methods=['GET', 'POST'])
def talks():
    if request.method == 'POST':
        payload = request.get_json(force=True, silent=True)
        return process_post_talk(payload)

    if request.method == 'GET':
        return process_get_talks()

@app.route('/talks/<talk_id>', methods=['GET'])
def talk(talk_id):
    ''' Returns info about a specific talk '''
    return process_user_get(talk_id)

def process_post_talk(payload):
    ''' Save talk into database and return talk id '''

    inserted_id = mongo_handler.persist_user(payload)
    print(f'process_post_talk: {inserted_id}')
    return json.dumps(inserted_id, cls=JSONEncoder)

def process_get_talks():
    ''' Return all talks from database '''

    talks = mongo_handler.get_users()
    json_users = json.dumps(talks, cls=JSONEncoder)
    print(f'process_get_talks: {json_users}')
    return json_users

def process_user_get(id):
    ''' Return talk from database '''

    talk = mongo_handler.get_user(id)
    json_user = json.dumps(talk, cls=JSONEncoder)
    return json_user

if __name__ == '__main__':
    app.run(port=5001, debug=True)