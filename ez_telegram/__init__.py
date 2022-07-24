from typing import List
from requests import get
from bs4 import BeautifulSoup as bs
from markdownify import markdownify

class Message:

    def __init__(self, content: str) -> None:
        self.__content = content

    @property
    def html(self) -> str:
        return self.__content
    
    @property
    def text(self) -> str:
        return markdownify(self.__content)

class EzClient:
    """ Simple client to get messages from a telegram channel by webscraping."""

    USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'

    def __init__(self, **kwargs) -> None:
        
        self.__url = 'https://t.me/s/{channel_name}'
        self.__headers = kwargs.get('headers', {})

    def _get(self, channel: str) -> bytes:

        self.__headers['User-Agent'] = self.USER_AGENT
        
        response = get(self.__url.format(channel_name=channel), headers=self.__headers, allow_redirects=True)
        if response.status_code == 200 and response.url == self.__url.format(channel_name=channel):
            return response.content

        raise ChannelNotFoundError(channel) if response.url != self.__url.format(channel_name=channel) else StatusCodeError(response.status_code)

    def get_messages(self, channel: str) -> List[str]:

        content: bytes = self._get(channel)
        messages: List[Message] = self.parse_messages(content)
        return list(messages)

    def parse_messages(self, content: bytes) -> List[Message]:

        document = bs(content, 'lxml')
        messages = document.find_all('div', class_='tgme_widget_message_wrap js-widget_message_wrap')

        for message in messages:
            yield Message(str(message)).text.replace('\n', '')

class ChannelNotFoundError(Exception):
    pass

class StatusCodeError(Exception):
    pass