import json

from channels.generic.websocket import AsyncWebsocketConsumer


class ChatsConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.chat_id = self.scope['url_route']['kwargs']['chat_id']
        self.chat_group_name = 'chat_%s' % self.chat_id

        await self.channel_layer.group_add(
            self.chat_group_name,
            self.channel_name
        )

    async def disconnect(self, code):
        await self.channel_layer.disconnect(
            self.chat_group_name,
            self.channel_name
        )
