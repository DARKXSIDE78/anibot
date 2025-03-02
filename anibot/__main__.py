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

from flask import Flask

flask_app = Flask(__name__)

# Create a health check route
@flask_app.route("/health")
def health_check():
    return "OK", 200

# Custom route to display your message
@flask_app.route("/")
def home():
    return "DARKXSIDE78 - The darkness shall follow my command", 200

# Run Flask app in a separate thread so it doesn't block the main bot process
import threading

def run_flask():
    flask_app.run(host='0.0.0.0', port=8000)

# Start the Flask app in a separate thread
flask_thread = threading.Thread(target=run_flask)
flask_thread.daemon = True
flask_thread.start()


asyncio.get_event_loop().run_until_complete(main())
