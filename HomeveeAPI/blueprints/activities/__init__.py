import json
import traceback

from flask import Blueprint, request
from werkzeug.exceptions import abort

from HomeveeAPI.blueprints.activities.ActivityManager import ActivityManager

ActivityAPI = Blueprint('ActivityAPI', __name__, template_folder='templates')

BASE_PATH = "/activities/"

@ActivityAPI.route(BASE_PATH+'random', methods=['GET'])
def get_random_activity():
    try:
        language = request.args.get("language")
        categories = request.args.get("categories")

        #parse category string to array

        return json.dumps(ActivityManager(language).get_random(categories))
    except:
        traceback.print_exc()
        abort(500)

@ActivityAPI.route(BASE_PATH+'random/<number>', methods=['GET'])
def get_random_activities(number):
    try:
        assert number == request.view_args['number']
        language = request.args.get("language")
        categories = request.args.get("categories")

        #parse category string to array

        return json.dumps(ActivityManager(language).get_random_multiple(categories, number))
    except:
        traceback.print_exc()
        abort(500)