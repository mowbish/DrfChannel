import asyncio
from django.conf import settings
from channels.generic.websocket import AsyncWebsocketConsumer, JsonWebsocketConsumer, WebsocketConsumer
from time import sleep
from random import randint
from kucoin.client import WsToken
from kucoin.ws_client import KucoinWsClient
from channels.layers import get_channel_layer

channel_layer = get_channel_layer()


async def main():
    # receive
    async def deal_msg(msg):
        if msg['topic'] == '/spotMarket/level2Depth5:BTC-USDT':
            print(msg["data"])
        elif msg['topic'] == '/spotMarket/level2Depth5:KCS-USDT':
            print(f'Get KCS level3:{msg["data"]}')

    # connect
    client = WsToken()

    # is private
    # client = WsToken(key='', secret='', passphrase='', is_sandbox=False, url='')
    # is sandbox
    # client = WsToken(is_sandbox=True)

    # send
    ws_client = await KucoinWsClient.create(None, client, deal_msg, private=False)
    # await ws_client.subscribe('/market/ticker:BTC-USDT,ETH-USDT')
    # send
    await ws_client.subscribe('/spotMarket/level2Depth5:BTC-USDT,KCS-USDT')
    # while True:
    #     await asyncio.sleep(60, loop=loop)


class WSConsumer(AsyncWebsocketConsumer):

    async def connect(self):

        # await self.channel_layer.group_add(
        #     await main()
        # )
        self.is_connected = True
        await self.accept()
        # await main()
        while True:
            self.send({
                "hello": "mobin"
            })
            # await asyncio.sleep(5)

    async def disconnect(self, close_code):
        self.is_connected = False

    # Receive message from WebSocket
    async def receive(self, text_data):
        # return await main()
        self.send({
            "hello": text_data
        })

    async def send(self, text_data=None, bytes_data=None, close=False):
        self.send({
            "hello": text_data
        })

    # async def show_result(self, event):

    #     await channel_layer.send("channel_name", {
    #         "type": "chat.message",
    #         "text": "Hello there!",
    #     })

    # async def show_asks(self, event):
    #     asks = event['asks']
    #     await self.send(asks)

# if __name__ == "currencies.consumers":
#     loop = asyncio.get_event_loop()
#     loop.run_until_complete(main())
