import json
import os
from dotenv import load_dotenv

load_dotenv()

from googleapiclient.discovery import build

api_key = os.getenv('API_KEY') # YT_API_KEY скопирован из гугла и вставлен в переменные окружения

youtube = build('youtube', 'v3', developerKey=api_key)# создать специальный объект для работы с API
class Channel:
    """Класс для ютуб-канала"""


    def __init__(self, channel_id) -> None:
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        self.channel_id = channel_id

    def print_info(self) -> None:
        """Выводит в консоль информацию о канале."""
        dict_channel = youtube.channels().list(id=self.channel_id, part='snippet,statistics').execute()
        print(print(json.dumps(dict_channel, indent=2, ensure_ascii=False)))
