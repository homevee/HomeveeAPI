from Utils.ServerData import ServerData


class WeatherManager:
    def __init__(self):
        return

    def get_weather(self, location):
        api_key = ServerData().get("OPEN_WEATHER_MAP_API_KEY")

        return {}

    def get_cities(self, keyword=None):
        return []