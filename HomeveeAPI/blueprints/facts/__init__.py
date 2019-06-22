import json
import traceback

from flask import Blueprint, request
from werkzeug.exceptions import abort

from HomeveeAPI.blueprints.facts.FactManager import FactManager

FactAPI = Blueprint('FactAPI', __name__, template_folder='templates')

BASE_PATH = "/facts/"

@FactAPI.route(BASE_PATH+'random', methods=['GET'])
def get_random_fact():
    try:
        language = request.args.get("language")
        categories = request.args.get("categories")

        #parse category string to array

        return json.dumps(FactManager(language).get_random(categories))
    except:
        traceback.print_exc()
        abort(500)