import json

from HomeveeAPI.Utils.CacheManager import CacheManager
from HomeveeAPI.Utils.ServerData import ServerData
import urllib.error
import urllib.parse
import urllib.request


class WeatherManager:
    def __init__(self):
        return

    def refresh_weather_cache(self, location, api_key):
        """
        Updates the weather cache for the given location
        :param location: the location
        :param api_key: the api key for the data source
        :return:
        """
        url = "http://api.openweathermap.org/data/2.5/forecast/daily?id=" + location\
              + "&cnt=16&units=metric&lang=de&type=accurate&APPID=" + api_key

        response = urllib.request.urlopen(url).read()

        CacheManager().write_cache("WEATHER", location, response)

        return response

    def get_weather(self, location):
        """
        Returns the current weather data for the given location
        :param location:
        :return:
        """
        api_key = ServerData().get("OPEN_WEATHER_MAP_API_KEY")

        data = CacheManager().read_cache("WEATHER", location)

        if data is None:
            data = self.refresh_weather_cache(location, api_key)

        #process weather data

        return json.loads(data)

    def get_cities(self, keyword=None):
        """
        Returns a list of cities identified by the keyword string
        :param keyword:
        :return:
        """
        return []