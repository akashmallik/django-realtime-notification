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
