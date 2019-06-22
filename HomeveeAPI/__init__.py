#!flask/bin/python
import argparse

from flask import Flask

from HomeveeAPI.blueprints.activities import ActivityAPI
from HomeveeAPI.blueprints.assistant import AssistantAPI
from HomeveeAPI.blueprints.devices import DevicesAPI
from HomeveeAPI.blueprints.facts import FactAPI
from HomeveeAPI.blueprints.food import FoodAPI
from HomeveeAPI.blueprints.jokes import JokesAPI
from HomeveeAPI.blueprints.tv import TVProgrammAPI
from HomeveeAPI.blueprints.weather import WeatherAPI

app = Flask(__name__)

blueprints = [AssistantAPI, JokesAPI, TVProgrammAPI, WeatherAPI, DevicesAPI, FoodAPI, FactAPI, ActivityAPI]

for blueprint in blueprints:
    app.register_blueprint(blueprint)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='API for Homevee')
    parser.add_argument('--dev', default=False, type=bool, help='Is the server in dev mode?')
    parser.add_argument('--test', default=False, type=bool, help='Is the server in test mode?')
    parser.add_argument('--domain', required=False, default="dev-test.homevee.de", type=str, help='The domain to run the api on')
    args = parser.parse_args()

    DEV_ENV = args.dev
    TEST_ENV = args.test

    HOST = args.domain

    if DEV_ENV:
        app.run(debug=True, threaded=True)
    elif TEST_ENV:
        HOST = "dev-test.homevee.de"

        CERT_FILE = "/etc/letsencrypt/live/" + HOST + "/cert.pem"
        CHAIN_FILE = "/etc/letsencrypt/live/" + HOST + "/chain.pem"
        FULLCHAIN_FILE = "/etc/letsencrypt/live/" + HOST + "/fullchain.pem"
        KEY_FILE = "/etc/letsencrypt/live/" + HOST + "/privkey.pem"

        app.run(host=HOST, port=7778, ssl_context=(FULLCHAIN_FILE, KEY_FILE), threaded=True)