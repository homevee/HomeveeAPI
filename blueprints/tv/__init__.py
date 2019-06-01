import json
import traceback

from flask import Blueprint
from blueprints.tv.TVProgrammManager import TVProgrammManager, TVItem

TVProgrammAPI = Blueprint('TVProgrammAPI', __name__, template_folder='templates')

BASE_PATH = "/tv/"

@TVProgrammAPI.route(BASE_PATH+'tipps', methods=['GET'])
def get_tv_tipps():
    items = TVProgrammManager().get_tv_programm("tipps")
    return json.dumps({'tvprogramm': TVItem.to_dict_list(items), 'type': 'tipps'})

@TVProgrammAPI.route(BASE_PATH+'2200', methods=['GET'])
def get_programme_2200():
    items = TVProgrammManager().get_tv_programm("heute2200")
    return json.dumps({'tvprogramm': TVItem.to_dict_list(items), 'type': '2200'})

@TVProgrammAPI.route(BASE_PATH+'2015', methods=['GET'])
def get_programme_2015():
    items = TVProgrammManager().get_tv_programm("heute2015")
    return json.dumps({'tvprogramm': TVItem.to_dict_list(items), 'type': '2015'})

@TVProgrammAPI.route(BASE_PATH+'jetzt', methods=['GET'])
def get_programme_now():
    items = TVProgrammManager().get_tv_programm("jetzt")
    return json.dumps({'tvprogramm': TVItem.to_dict_list(items), 'type': 'jetzt'})

@TVProgrammAPI.route(BASE_PATH+'channels', methods=['GET'])
def get_channels():
    items = TVProgrammManager().get_tv_programm("jetzt")
    return json.dumps({'channels': TVProgrammManager().get_channels()})