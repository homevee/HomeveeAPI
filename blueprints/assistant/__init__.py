import traceback

from flask import Blueprint
from werkzeug.exceptions import abort

from blueprints.assistant.Assistant import Assistant

AssistantAPI = Blueprint('AssistantAPI', __name__, template_folder='templates')

BASE_PATH = "/assistant/"

@AssistantAPI.route(BASE_PATH+'handleVoiceCommand', methods=['GET'])
def handle_plain_text():
    try:
        return Assistant().handle_voice_command()
    except:
        traceback.print_exc()
        abort(500)