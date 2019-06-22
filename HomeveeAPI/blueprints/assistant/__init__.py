import traceback

from flask import Blueprint, request
from werkzeug.exceptions import abort

from HomeveeAPI.blueprints.assistant.Assistant import Assistant

AssistantAPI = Blueprint('AssistantAPI', __name__, template_folder='templates')

BASE_PATH = "/assistant/"

@AssistantAPI.route(BASE_PATH+'voicecommand', methods=['GET'])
def handle_voice_command():
    try:
        language = request.args.get("language")
        command = request.args.get("command")
        return Assistant(language).handle_voice_command(command)
    except:
        traceback.print_exc()
        abort(500)

@AssistantAPI.route(BASE_PATH+'classify', methods=['GET'])
def classify_voice_command():
    try:
        language = request.args.get("language")
        command = request.args.get("command")
        return Assistant(language).classify_voice_command(command)
    except:
        traceback.print_exc()
        abort(500)