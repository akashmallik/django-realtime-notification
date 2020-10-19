import asyncio

from channels.consumer import AsyncConsumer
from channels.generic.websocket import AsyncJsonWebsocketConsumer


class EchoConsumer(AsyncConsumer):

    async def websocket_connect(self, event):
        await self.send({
            "type": "websocket.accept",
        })

    async def websocket_receive(self, event):
        await self.send({
            "type": "websocket.send",
            "text": event["text"],
        })


class TickTockConsumer(AsyncJsonWebsocketConsumer):
    async def connect(self):
        await self.accept()
        while True:
            await asyncio.sleep(1)
            await self.send_json("tick")
            await asyncio.sleep(1)
            await self.send_json("....tock")


class NotificationConsumer(AsyncJsonWebsocketConsumer):

    async def connect(self):
        await self.accept()
        await self.channel_layer.group_add("gossip", self.channel_name)

    async def disconnect(self, code):
        await self.channel_layer.group_discard("gossip", self.channel_name)

    async def user_gossip(self, event):
        await self.send_json(event)
