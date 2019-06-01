import traceback

from flask import Blueprint, request
from werkzeug.exceptions import abort

from blueprints.food.FoodManager import FoodManager

FoodAPI = Blueprint('FoodAPI', __name__, template_folder='templates')

BASE_PATH = "/food/"

@FoodAPI.route(BASE_PATH+'search/<keyword>', methods=['GET'])
def search_food(keyword):
    try:
        assert keyword == request.view_args['keyword']
        return FoodManager().search_food(keyword)
    except:
        traceback.print_exc()
        abort(500)