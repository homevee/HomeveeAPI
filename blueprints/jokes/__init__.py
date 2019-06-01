import traceback

from flask import Blueprint, request
from werkzeug.exceptions import abort

from blueprints.jokes.JokeManager import JokeManager

JokesAPI = Blueprint('JokesAPI', __name__, template_folder='templates')

BASE_PATH = "/jokes/"

@JokesAPI.route(BASE_PATH+'random', methods=['GET'])
def get_random_joke(language):
    try:
        language = request.args.get("language")
        categories = request.args.get("categories")

        #parse category string to array

        return JokeManager(language).get_random_joke(categories)
    except:
        traceback.print_exc()
        abort(500)