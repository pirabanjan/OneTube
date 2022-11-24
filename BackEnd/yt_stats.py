import requests
import json

class YTStats:

    def __init__(self, api_key, channel_id):
        self.API_Key= api_key
        self.channel_id=channel_id
        self.channel_stats=None

    def get_stats(self):
        url = f'https://www.googleapis.com/youtube/v3/channels?part=statistics&id={self.channel_id}&key={self.API_Key}'
        print(url)
        json_url = requests.get(url)
        data = json.loads(json_url.text)
        print(data)