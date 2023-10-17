import json
import os
from dotenv import load_dotenv

load_dotenv()

from googleapiclient.discovery import build


class Channel:
    """Класс для ютуб-канала"""
    api_key = os.getenv('YT_API_KEY')  # API_KEY скопирован из гугла и вставлен в переменные окружения
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


    def __str__(self):
         return f'{self.title},{self.url}'

    def __add__(self, other):
            return int(self.subscriber_count) + int(other.subscriber_count)

    def __sub__(self, other):
            return int(self.subscriber_count) - int(other.subscriber_count)

    def __gt__(self, other):
            return self.subscriber_count > other.subscriber_count

    def __ge__(self, other):
            return self.subscriber_count >= other.subscriber_count


    def __lt__(self, other):
            return self.subscriber_count < other.subscriber_count

    def __le__(self, other):
            return self.subscriber_count <= other.subscriber_count

    def __eq__(self, other):
            return self.subscriber_count == other.subscriber_count

    @staticmethod
    def printj(dict_to_print) -> None:
            """Выводит словарь в json-подобном удобном формате с отступами"""
            print(json.dumps(dict_to_print, indent=2, ensure_ascii=False))


    def print_info(self) -> None:
        """Выводит в консоль информацию о  канале."""
        self.printj(self.channel)

    @property
    def channel_id(self):
        """Возвращает id канала"""
        return self.__channel_id

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
            json.dump(data, file, ensure_ascii=False, indent=4)
