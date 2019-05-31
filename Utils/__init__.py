import json


class Utils:
    def __init__(self):
        return

    @staticmethod
    def get_config_data():
        """
        Loads the stored config data from the servers config file
        :return:
        """
        with open('/homevee_api_data/config.json') as json_file:
            data = json.load(json_file)
            return data