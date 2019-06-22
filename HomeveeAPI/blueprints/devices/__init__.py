import traceback

from flask import Blueprint, request
from werkzeug.exceptions import abort

from HomeveeAPI.blueprints.devices.DeviceManager import DeviceManager

DevicesAPI = Blueprint('DevicesAPI', __name__, template_folder='templates')

BASE_PATH = "/devices/"

@DevicesAPI.route(BASE_PATH, methods=['GET'])
def search_food():
    try:
        return DeviceManager().get_devices()
    except:
        traceback.print_exc()
        abort(500)