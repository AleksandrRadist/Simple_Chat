import json


from channels.db import database_sync_to_async
from channels.generic.websocket import AsyncWebsocketConsumer

from .models import Chat, Message


class ChatsConsumer(AsyncWebsocketConsumer):

    async def connect(self):
        self.chat_id = self.scope['url_route']['kwargs']['chat_id']
        self.chat_group_name = 'chat_%s' % self.chat_id

        # Join room group
        await self.channel_layer.group_add(
            self.chat_group_name,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self, close_code):
        # Leave room group
        await self.channel_layer.group_discard(
            self.chat_group_name,
            self.channel_name
        )

    # Receive message from WebSocket
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['text']
        new_message = await self.create_new_message(message)
        data = {'author': new_message.author.username,
                'pub_date': new_message.pub_date.strftime('%Y-%m-%d %H:%m'),
                'text': new_message.text}
        # Send message to room group
        await self.channel_layer.group_send(
            self.chat_group_name,
            {
                'type': 'new_message',
                'message': data
            }
        )

    # Receive message from room group
    async def new_message(self, event):
        message = event['message']

        # Send message to WebSocket
        await self.send(text_data=json.dumps({
            'message': message
        }))

    @database_sync_to_async
    def create_new_message(self, text):
        chat = Chat.objects.get(id=self.chat_id)
        new_message = Message.objects.create(
            author=self.scope['user'],
            text=text,
            chat=chat
        )
        return new_message
