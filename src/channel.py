import json
import os
from dotenv import load_dotenv

load_dotenv()

from googleapiclient.discovery import build


class Channel:
    """Класс для ютуб-канала"""
    api_key = os.getenv('API_KEY')  # YT_API_KEY скопирован из гугла и вставлен в переменные окружения
    youtube = build('youtube', 'v3', developerKey=api_key)  # создать специальный объект для работы с API

    def __init__(self, channel_id) -> None:
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        self.__channel_id = channel_id
        self.channel = self.youtube.channels().list(id=self.channel_id, part='snippet,statistics').execute()
        self.title = self.channel['items'][0]['snippet']['title']
        self.description = self.channel['items'][0]['snippet']['description']
        self.url = 'https://www.youtube.com/channel/' + self.channel_id
        self.subscriber_count = self.channel['items'][0]['statistics']['subscriberCount']
        self.view_count = self.channel['items'][0]['statistics']['viewCount']
        self.video_count = self.channel['items'][0]['statistics']['videoCount']

    def print_info(self) -> None:
        """Выводит в консоль информацию о канале."""
        self.printj(self.channel)

    @classmethod
    def get_service(cls):
        return cls.youtube

    def to_json(self, filename):
        with open(filename, 'w', encoding='utf-8') as file:
            data = {
                'channel_id': self.channel_id,
                'title': self.title,
                'description': self.description,
                'url': self.url,
                'subscriber_count': self.subscriber_count,
                'view_count': self.view_count,
                'video_count': self.video_count
            }
            json.dump(data, file, ensure_ascii=False)
