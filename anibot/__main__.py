import asyncio
from pyrogram import idle
from . import anibot, has_user, session
from .utils.db import _close_db

user = None
if has_user:
    from . import user

async def main():
    await anibot.start()
    if user is not None:
        await user.start()
    await idle()
    await anibot.stop()
    if user is not None:
        await user.stop()
    _close_db()
    await session.close()

from aiohttp import web

routes = web.RouteTableDef()

@routes.get("/", allow_head=True)
async def root_route_handler(request):
    return web.json_response("DARKXSIDE78 - The darkness shall follow my command")

@routes.get("/health", allow_head=True)
async def health_check(request):
    return web.json_response({"status": "OK"})

async def web_server():
    web_app = web.Application(client_max_size=30000000)
    web_app.add_routes(routes)
    runner = web.AppRunner(web_app)
    await runner.setup()
    site = web.TCPSite(runner, "0.0.0.0", 8000)
    await site.start()
    print("Web server started at http://0.0.0.0:8000")

async def run_all():
    await asyncio.gather(main(), web_server())

if __name__ == "__main__":
    asyncio.run(run_all())
