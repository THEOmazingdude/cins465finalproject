# chat/consumers.py
import json
from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer
from . import models

class ChatConsumer(WebsocketConsumer):
    def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'chat_%s' % self.room_name

        # Join room group
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )

        self.accept()

    def disconnect(self, close_code):
        # Leave room group
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name,
            self.channel_name
        )

    # Receive message from WebSocket
    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        type = text_data_json['type']
        source = text_data_json['source']
        dest = text_data_json['dest']
        message = text_data_json['message']

        # Send message to room group
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                'type': type,
                'source': source,
                'dest': dest,
                'message': message
            }
        )

    # Receive message from room group
    def chat_message(self, event):
        type = event['type'],
        source = event['source'],
        dest = event['source'],
        message = event['message']

        # Send message to WebSocket
        self.send(text_data=json.dumps({
            'type': type,
            'source': source,
            'dest': dest,
            'message': message
        }))

    # Receive message from room group
    def move(self, event):
        type = event['type'],
        source = event['source']
        dest = event['dest'],
        message = event['message']

        # Send message to WebSocket
        self.send(text_data=json.dumps({
            'type': type,
            'source': source,
            'dest': dest,
            'message': message
        }))