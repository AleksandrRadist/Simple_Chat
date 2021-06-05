from django.urls import re_path

from . import consumers

websocket_urlpatterns = [
    re_path(r'chats/(?P<chat_id>\d+)/$)', consumers.ChatsConsumer.as_asgi())
]