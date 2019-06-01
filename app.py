#!flask/bin/python
import argparse
import json

from flask import Flask, jsonify, abort, request

from Utils import Utils
from blueprints.assistant import AssistantAPI
from blueprints.devices import DevicesAPI
from blueprints.food import FoodAPI
from blueprints.jokes import JokesAPI
from blueprints.tv import TVProgrammAPI
from blueprints.weather import WeatherAPI

app = Flask(__name__)

@app.route('/all', methods=['GET'])
def get_tasks():
    return json.dumps({'tasks': ""})

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='API for Homevee')
    parser.add_argument('--dev', default=False, type=bool, help='Is the server in dev mode?')
    args = parser.parse_args()
    DEV_ENV = args.dev

    blueprints = [AssistantAPI, JokesAPI, TVProgrammAPI, WeatherAPI, DevicesAPI, FoodAPI]

    for blueprint in blueprints:
        app.register_blueprint(blueprint)

    if DEV_ENV:
        app.run(debug=True)
    else:
        HOST = "api.homevee.de"

        CERT_FILE = "/etc/letsencrypt/live/"+HOST+"/cert.pem"
        KEY_FILE = "/etc/letsencrypt/live/"+HOST+"/privkey.pem"

        app.config['SERVER_NAME'] = HOST

        app.run(host=HOST, port=443, ssl_context=(CERT_FILE, KEY_FILE))