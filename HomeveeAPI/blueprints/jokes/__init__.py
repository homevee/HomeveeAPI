import json
import traceback

from flask import Blueprint, request
from werkzeug.exceptions import abort

from HomeveeAPI.blueprints.jokes.JokeManager import JokeManager

JokesAPI = Blueprint('JokesAPI', __name__, template_folder='templates')

BASE_PATH = "/jokes/"

@JokesAPI.route(BASE_PATH+'random', methods=['GET'])
def get_random_joke():
    try:
        language = request.args.get("language")
        categories = request.args.get("categories")

        #parse category string to array

        return json.dumps(JokeManager(language).get_random(categories))
    except:
        traceback.print_exc()
        abort(500)