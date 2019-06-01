import traceback

from flask import Blueprint, request
from werkzeug.exceptions import abort

from blueprints.jokes.JokeManager import JokeManager

JokesAPI = Blueprint('JokesAPI', __name__, template_folder='templates')

BASE_PATH = "/jokes/"

@JokesAPI.route(BASE_PATH+'random/<language>', methods=['GET'])
def get_random_joke(language):
    try:
        assert language == request.view_args['remote_id']
        return JokeManager(language).get_random_joke()
    except:
        traceback.print_exc()
        abort(500)

@JokesAPI.route(BASE_PATH+'random/<language>/<categories>', methods=['GET'])
def get_random_joke_by_category(language, categories):
    try:
        assert language == request.view_args['remote_id']
        assert categories == request.view_args['categories']

        #parse category string to array

        return JokeManager(language).get_random_joke(categories)
    except:
        traceback.print_exc()
        abort(500)