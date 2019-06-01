import traceback

from flask import Blueprint, request
from werkzeug.exceptions import abort

from blueprints.assistant.Assistant import Assistant

AssistantAPI = Blueprint('AssistantAPI', __name__, template_folder='templates')

BASE_PATH = "/assistant/"

@AssistantAPI.route(BASE_PATH+'handleVoiceCommand/<language>/<command>', methods=['GET'])
def handle_voice_command(language, command):
    try:
        assert language == request.view_args['remote_id']
        assert command == request.view_args['command']
        return Assistant(language).handle_voice_command(command)
    except:
        traceback.print_exc()
        abort(500)

@AssistantAPI.route(BASE_PATH+'handleVoiceCommand/<language>/<command>', methods=['GET'])
def classify_voice_command(language, command):
    try:
        assert language == request.view_args['remote_id']
        assert command == request.view_args['command']
        return Assistant(language).classify_voice_command(command)
    except:
        traceback.print_exc()
        abort(500)