import logging
import asyncio
from aiohttp import web

logging.basicConfig(level=logging.INFO)

async def index(request):
    #定义服务器响应请求的返回为'Awesome Website'
    return web.Response(body=b'<h1>Awesome Website</h1>',content_type='text/html')

def init():
    #建立服务器应用，持续监听本地9000端口的http请求，对首页/进行响应
    app=web.Application()
    app.router.add_get('/',index)
    web.run_app(app,host='127.0.0.1',port=9000)

if __name__ == '__main__':
    init()

