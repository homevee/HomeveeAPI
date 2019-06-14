#!flask/bin/python
import argparse
import json

from flask import Flask, jsonify, abort, request
from werkzeug.utils import redirect

from Utils import Utils
from blueprints.activities import ActivityAPI
from blueprints.assistant import AssistantAPI
from blueprints.devices import DevicesAPI
from blueprints.facts import FactAPI
from blueprints.food import FoodAPI
from blueprints.jokes import JokesAPI
from blueprints.tv import TVProgrammAPI
from blueprints.weather import WeatherAPI

app = Flask(__name__)

@app.before_request
def before_request():
    if not DEV_ENV and request.url.startswith('http://'):
        url = request.url.replace('http://', 'https://', 1)
        code = 301
        return redirect(url, code=code)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='API for Homevee')
    parser.add_argument('--dev', default=False, type=bool, help='Is the server in dev mode?')
    parser.add_argument('--test', default=False, type=bool, help='Is the server in test mode?')
    parser.add_argument('--domain', required=False, default="dev-test.homevee.de", type=str, help='The domain to run the api on')
    args = parser.parse_args()

    DEV_ENV = args.dev
    TEST_ENV = args.test

    HOST = args.domain

    blueprints = [AssistantAPI, JokesAPI, TVProgrammAPI, WeatherAPI, DevicesAPI, FoodAPI, FactAPI, ActivityAPI]

    for blueprint in blueprints:
        app.register_blueprint(blueprint)

    if DEV_ENV:
        app.run(debug=True, threaded=True)
    elif TEST_ENV:
        HOST = "dev-test.homevee.de"

        CERT_FILE = "/etc/letsencrypt/live/" + HOST + "/cert.pem"
        CHAIN_FILE = "/etc/letsencrypt/live/" + HOST + "/chain.pem"
        FULLCHAIN_FILE = "/etc/letsencrypt/live/" + HOST + "/fullchain.pem"
        KEY_FILE = "/etc/letsencrypt/live/" + HOST + "/privkey.pem"

        app.run(host=HOST, port=7778, ssl_context=(FULLCHAIN_FILE, KEY_FILE), threaded=True)
    else:
        HOST = "api.homevee.de"

        CERT_FILE = "/etc/letsencrypt/live/" + HOST + "/cert.pem"
        CHAIN_FILE = "/etc/letsencrypt/live/" + HOST + "/chain.pem"
        FULLCHAIN_FILE = "/etc/letsencrypt/live/" + HOST + "/fullchain.pem"
        KEY_FILE = "/etc/letsencrypt/live/" + HOST + "/privkey.pem"

        app.config['SERVER_NAME'] = HOST

        app.run(host=HOST, port=443, ssl_context=(FULLCHAIN_FILE, KEY_FILE), threaded=True)