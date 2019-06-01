import traceback

from flask import Blueprint, request
from werkzeug.exceptions import abort

from blueprints.weather.WeatherManager import WeatherManager

WeatherAPI = Blueprint('WeatherAPI', __name__, template_folder='templates')

BASE_PATH = "/weather/"

@WeatherAPI.route(BASE_PATH+'/<location>', methods=['GET'])
def get_weather(location):
    try:
        assert location == request.view_args['location']
        return WeatherManager().get_weather(location)
    except:
        traceback.print_exc()
        abort(500)

@WeatherAPI.route(BASE_PATH+'/cities/<keyword>', methods=['GET'])
def get_cities(keyword):
    try:
        assert keyword == request.view_args['keyword']
        return WeatherManager().get_cities(keyword)
    except:
        traceback.print_exc()
        abort(500)