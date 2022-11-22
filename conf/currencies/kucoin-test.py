import asyncio

#api_key = '6377ec601efec4000139f032'
#api_secret = '76dc52a1-35f1-49d9-8d2b-97d9759d1760'
#api_passphrase = 'mmoobbiinn'
"""
    install this pakage using:
        pip3 install kucoin-python
"""
from kucoin.client import WsToken
from kucoin.ws_client import KucoinWsClient


async def main():
    # receive
    async def deal_msg(msg):
        if msg['topic'] == '/spotMarket/level2Depth5:BTC-USDT':
            print(msg["data"])
        elif msg['topic'] == '/spotMarket/level2Depth5:KCS-USDT':
            print(f'Get KCS level3:{msg["data"]}')

    # connect
    client = WsToken()

    #is private
    # client = WsToken(key='', secret='', passphrase='', is_sandbox=False, url='')
    # is sandbox
    # client = WsToken(is_sandbox=True)

    # send
    ws_client = await KucoinWsClient.create(None, client, deal_msg, private=False)
    #await ws_client.subscribe('/market/ticker:BTC-USDT,ETH-USDT')
    # send
    await ws_client.subscribe('/spotMarket/level2Depth5:BTC-USDT,KCS-USDT')
    while True:
        await asyncio.sleep(60, loop=loop)


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
