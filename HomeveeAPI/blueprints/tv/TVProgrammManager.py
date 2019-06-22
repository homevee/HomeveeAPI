import json
import urllib.error
import urllib.parse
import urllib.request
import xml.etree.ElementTree as etree

from HomeveeAPI.Utils.CacheManager import CacheManager


class TVProgrammManager():
    def __init__(self):
        return

    def get_tv_programm(self, type):
        data = CacheManager().read_cache("TV_PROGRAMM", type)

        print(data)

        if data is None:
            #if not use_cache:
            #    return None

            link = "http://www.tvspielfilm.de/tv-programm/rss/" + type + ".xml"

            print(link)

            try:
                file = urllib.request.urlopen(link)
                data = file.read()
                file.close()
                CacheManager().write_cache("TV_PROGRAMM", type, data)
            except:
                return None

        return self.parse_api_data(data)

    def parse_api_data(self, data):
        tv_shows = []

        # XML-Datei laden
        ergebnis = etree.fromstring(data)

        for item in ergebnis.find('channel').findall('item'):
            time, channel, name = item.find('title').text.split(" | ")

            description = item.find('description').text

            img = None
            if item.find('image') is not None:
                img = item.find('image').attrib['url']

            tv_shows.append(TVItem(name, time, channel, img, description))

        return tv_shows

    def get_channels(self):
        data = CacheManager().read_cache("TV_PROGRAMM", "channels", max_time=60*60*24)
        if data is None:
            items = []

            types = ['jetzt', 'tipps', 'heute2015', 'heute2200']

            for type in types:
                data = self.get_tv_programm(type)

                if data is not None:
                    items.extend(data)

            channels = []

            for item in items:
                if item.channel not in channels:
                    channels.append(item.channel)

            CacheManager().write_cache("TV_PROGRAMM", "channels", json.dumps(channels))
        else:
            channels = json.loads(data)

        return channels


class TVItem():
    def __init__(self, name, time, channel, img, description):
        self.name = name
        self.time = time
        self.channel = channel
        self.img = img
        self.descritpion = description

    def to_dict(self):
        dict = {}

        dict['name'] = self.name
        dict['time'] = self.time
        dict['channel'] = self.channel
        dict['img'] = self.img
        dict['description'] = self.descritpion

        return dict

    @staticmethod
    def to_dict_list(list):
        if list is None:
            return None

        output = []

        for item in list:
            output.append(item.to_dict())

        return output