import os
from pyrogram import Client
from aiohttp import ClientSession

TRIGGERS = os.environ.get("TRIGGERS", "/ !").split()
API_HASH = os.environ.get("API_HASH", "f8a1b21a13af154596e2ff5bed164860")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "7899837889:AAFhqBW3SkJBUmuYeMDaIYDLbGqJPfCq4Zs")
BOT_NAME = os.environ.get("BOT_NAME", "@Komi")
DB_URL = os.environ.get("DATABASE_URL", "mongodb+srv://nitinkumardhundhara:DARKXSIDE78@cluster0.wdive.mongodb.net/?retryWrites=true&w=majority")
ANILIST_CLIENT = os.environ.get("ANILIST_CLIENT", "22243")
ANILIST_SECRET = os.environ.get("ANILIST_SECRET", "dXoehrRTH3ycbAIrSVAu69Gd7yhvmhvjZy4BldY1")
ANILIST_REDIRECT_URL = os.environ.get("ANILIST_REDIRECT_URL", "https://anilist.co/api/v2/oauth/pin")
API_ID = int(os.environ.get("API_ID", "10471716"))
LOG_CHANNEL_ID = os.environ.get("LOG_CHANNEL_ID", "@teteetetsss")
OWNER = list(filter(lambda x: x, map(int, os.environ.get("OWNER_ID", "1005170481 804248372 1993696756 7086472788").split())))  ## sudos can be included

DOWN_PATH = "anibot/downloads/"
HELP_DICT = dict()

session = ClientSession()
plugins = dict(root="anibot/plugins")
anibot = Client("anibot", bot_token=BOT_TOKEN, api_id=API_ID, api_hash=API_HASH, plugins=plugins)

has_user: bool = False
if os.environ.get('USER_SESSION'):
    has_user: bool = True
    user = Client(os.environ.get('USER_SESSION'), api_id=API_ID, api_hash=API_HASH)

HELP_DICT['Gʀᴏᴜᴘ'] = '''
Gʀᴏᴜᴘ ʙᴀsᴇᴅ ᴄᴏᴍᴍᴀɴᴅs:

/settings - Tᴏɢɢʟᴇ sᴛᴜғғ ʟɪᴋᴇ ᴡʜᴇᴛʜᴇʀ ᴛᴏ ᴀʟʟᴏᴡ 18+ sᴛᴜғғ ɪɴ ɢʀᴏᴜᴘ ᴏʀ ᴡʜᴇᴛʜᴇʀ ᴛᴏ ɴᴏᴛɪғʏ ᴀʙᴏᴜᴛ ᴀɪʀᴇᴅ ᴀɴɪᴍᴇs, ᴇᴛᴄ ᴀɴᴅ ᴄʜᴀɴɢᴇ UI
/disable - Dɪsᴀʙʟᴇ ᴜsᴇ ᴏғ ᴀ ᴄᴍᴅ ɪɴ ᴛʜᴇ ɢʀᴏᴜᴘ (Dɪsᴀʙʟᴇ ᴍᴜʟᴛɪᴘʟᴇ ᴄᴍᴅs ʙʏ ᴀᴅᴅɪɴɢ sᴘᴀᴄᴇ ʙᴇᴛᴡᴇᴇɴ ᴛʜᴇᴍ)
`/disable ᴀɴɪᴍᴇ ᴀɴɪʟɪsᴛ ᴍᴇ ᴜsᴇʀ`
/enable - Eɴᴀʙʟᴇ ᴜsᴇ ᴏғ ᴀ ᴄᴍᴅ ɪɴ ᴛʜᴇ ɢʀᴏᴜᴘ (Eɴᴀʙʟᴇ ᴍᴜʟᴛɪᴘʟᴇ ᴄᴍᴅs ʙʏ ᴀᴅᴅɪɴɢ sᴘᴀᴄᴇ ʙᴇᴛᴡᴇᴇɴ ᴛʜᴇᴍ)
`/enable ᴀɴɪᴍᴇ ᴀɴɪʟɪsᴛ ᴍᴇ ᴜsᴇʀ`
/disabled - Lɪsᴛ ᴏᴜᴛ ᴅɪsᴀʙʟᴇᴅ ᴄᴍᴅs
'''

HELP_DICT["Aᴅᴅɪᴛɪᴏɴᴀʟ"] = """Usᴇ /reverse ᴄᴍᴅ ᴛᴏ ɢᴇᴛ ʀᴇᴠᴇʀsᴇ sᴇᴀʀᴄʜ ᴠɪᴀ ᴛʀᴀᴄᴇᴍᴏᴇᴘʏ API
__Nᴏᴛᴇ: Tʜɪs ᴡᴏʀᴋs ʙᴇsᴛ ᴏɴ ᴜɴᴄʀᴏᴘᴘᴇᴅ ᴀɴɪᴍᴇ ᴘɪᴄ,
ᴡʜᴇɴ ᴜsᴇᴅ ᴏɴ ᴄʀᴏᴘᴘᴇᴅ ᴍᴇᴅɪᴀ, ʏᴏᴜ ᴍᴀʏ ɢᴇᴛ ʀᴇsᴜʟᴛ ʙᴜᴛ ɪᴛ ᴍɪɢʜᴛ ɴᴏᴛ ʙᴇ ᴛᴏᴏ ʀᴇʟɪᴀʙʟᴇ__
Usᴇ /schedule ᴄᴍᴅ ᴛᴏ ɢᴇᴛ sᴄʜᴇᴅᴜʟᴇᴅ ᴀɴɪᴍᴇs ʙᴀsᴇᴅ ᴏɴ ᴡᴇᴇᴋᴅᴀʏs.
Usᴇ /watch ᴄᴍᴅ ᴛᴏ ɢᴇᴛ ᴡᴀᴛᴄʜ ᴏʀᴅᴇʀ ᴏғ sᴇᴀʀᴄʜᴇᴅ ᴀɴɪᴍᴇ.
Usᴇ /fillers ᴄᴍᴅ ᴛᴏ ɢᴇᴛ ᴀ ʟɪsᴛ ᴏғ ғɪʟʟᴇʀs ғᴏʀ ᴀɴ ᴀɴɪᴍᴇ.
"""

HELP_DICT["Aɴɪʟɪsᴛ"] = """
**Bᴇʟᴏᴡ ɪs ᴛʜᴇ ʟɪsᴛ ᴏғ ʙᴀsɪᴄ ᴀɴɪʟɪsᴛ ᴄᴍᴅs ғᴏʀ ɪɴғᴏ ᴏɴ ᴀɴɪᴍᴇ, ᴄʜᴀʀᴀᴄᴛᴇʀ, ᴍᴀɴɢᴀ, ᴇᴛᴄ.

/anime - Usᴇ ᴛʜɪs ᴄᴍᴅ ᴛᴏ ɢᴇᴛ ɪɴғᴏ ᴏɴ sᴘᴇᴄɪғɪᴄ ᴀɴɪᴍᴇ ᴜsɪɴɢ ᴋᴇʏᴡᴏʀᴅs (ᴀɴɪᴍᴇ ɴᴀᴍᴇ) ᴏʀ Aɴɪʟɪsᴛ ID
(Cᴀɴ ʟᴏᴏᴋᴜᴘ ɪɴғᴏ ᴏɴ sᴇǫᴜᴇʟs ᴀɴᴅ ᴘʀᴇǫᴜᴇʟs)

/anilist - Usᴇ ᴛʜɪs ᴄᴍᴅ ᴛᴏ ᴄʜᴏᴏsᴇ ʙᴇᴛᴡᴇᴇɴ ᴍᴜʟᴛɪᴘʟᴇ ᴀɴɪᴍᴇs ᴡɪᴛʜ sɪᴍɪʟᴀʀ ɴᴀᴍᴇs ʀᴇʟᴀᴛᴇᴅ ᴛᴏ sᴇᴀʀᴄʜᴇᴅ ǫᴜᴇʀʏ
(Dᴏᴇsɴ'ᴛ ɪɴᴄʟᴜᴅᴇs ʙᴜᴛᴛᴏɴs ғᴏʀ ᴘʀᴇǫᴜᴇʟ ᴀɴᴅ sᴇǫᴜᴇʟ)

/character - Usᴇ ᴛʜɪs ᴄᴍᴅ ᴛᴏ ɢᴇᴛ ɪɴғᴏ ᴏɴ ᴄʜᴀʀᴀᴄᴛᴇʀ

/manga - Usᴇ ᴛʜɪs ᴄᴍᴅ ᴛᴏ ɢᴇᴛ ɪɴғᴏ ᴏɴ ᴍᴀɴɢᴀ

/airing - Usᴇ ᴛʜɪs ᴄᴍᴅ ᴛᴏ ɢᴇᴛ ɪɴғᴏ ᴏɴ ᴀɪʀɪɴɢ sᴛᴀᴛᴜs ᴏғ ᴀɴɪᴍᴇ

/top - Usᴇ ᴛʜɪs ᴄᴍᴅ ᴛᴏ ʟᴏᴏᴋᴜᴘ ᴛᴏᴘ ᴀɴɪᴍᴇs ᴏғ ᴀ ɢᴇɴʀᴇ/ᴛᴀɢ ᴏʀ ғʀᴏᴍ ᴀʟʟ ᴀɴɪᴍᴇs
(Tᴏ ɢᴇᴛ ᴀ ʟɪsᴛ ᴏғ ᴀᴠᴀɪʟᴀʙʟᴇ ᴛᴀɢs ᴏʀ ɢᴇɴʀᴇs sᴇɴᴅ /gettags ᴏʀ /getgenres
'/gettags ɴsғᴡ' ғᴏʀ ɴsғᴡ ᴛᴀɢs)

/user - Usᴇ ᴛʜɪs ᴄᴍᴅ ᴛᴏ ɢᴇᴛ ɪɴғᴏ ᴏɴ ᴀɴ ᴀɴɪʟɪsᴛ ᴜsᴇʀ

/browse - Usᴇ ᴛʜɪs ᴄᴍᴅ ᴛᴏ ɢᴇᴛ ᴜᴘᴅᴀᴛᴇs ᴀʙᴏᴜᴛ ʟᴀᴛᴇsᴛ ᴀɴɪᴍᴇs**
"""

HELP_DICT["Oᴀᴜᴛʜ"] = """
**Tʜɪs ɪɴᴄʟᴜᴅᴇs ᴀᴅᴠᴀɴᴄᴇᴅ ᴀɴɪʟɪsᴛ ғᴇᴀᴛᴜʀᴇs

Usᴇ /auth ᴏʀ !auth ᴄᴍᴅ ᴛᴏ ɢᴇᴛ ᴅᴇᴛᴀɪʟs ᴏɴ ʜᴏᴡ ᴛᴏ ᴀᴜᴛʜᴏʀɪᴢᴇ ʏᴏᴜʀ Aɴɪʟɪsᴛ ᴀᴄᴄᴏᴜɴᴛ ᴡɪᴛʜ ʙᴏᴛ
Aᴜᴛʜᴏʀɪsɪɴɢ ʏᴏᴜʀsᴇʟғ ᴜɴʟᴏᴄᴋs ᴀᴅᴠᴀɴᴄᴇᴅ ғᴇᴀᴛᴜʀᴇs ᴏғ ʙᴏᴛ ʟɪᴋᴇ:
- ᴀᴅᴅɪɴɢ ᴀɴɪᴍᴇ/character/manga ᴛᴏ ғᴀᴠᴏᴜʀɪᴛᴇs
- ᴠɪᴇᴡɪɴɢ ʏᴏᴜʀ ᴀɴɪʟɪsᴛ ᴅᴀᴛᴀ ʀᴇʟᴀᴛᴇᴅ ᴛᴏ ᴀɴɪᴍᴇ/ᴍᴀɴɢᴀ ɪɴ ʏᴏᴜʀ sᴇᴀʀᴄʜᴇs ᴡʜɪᴄʜ ɪɴᴄʟᴜᴅᴇs sᴄᴏʀᴇ, sᴛᴀᴛᴜs, ᴀɴᴅ ғᴀᴠᴏᴜʀɪᴛᴇs
- ᴜɴʟᴏᴄᴋ /flex, /me, /activaity ᴀɴᴅ /favourites ᴄᴏᴍᴍᴀɴᴅs
- ᴀᴅᴅɪɴɢ/ᴜᴘᴅᴀᴛɪɴɢ ᴀɴɪʟɪsᴛ ᴇɴᴛʀʏ ʟɪᴋᴇ ᴄᴏᴍᴘʟᴇᴛᴇᴅ ᴏʀ ᴘʟᴀɴ ᴛᴏ ᴡᴀᴛᴄʜ/ʀᴇᴀᴅ
- ᴅᴇʟᴇᴛɪɴɢ ᴀɴɪʟɪsᴛ ᴇɴᴛʀʏ

Usᴇ /flex ᴏʀ !flex ᴄᴍᴅ ᴛᴏ ɢᴇᴛ ʏᴏᴜʀ ᴀɴɪʟɪsᴛ sᴛᴀᴛs.
Usᴇ /logout ᴏʀ !logout ᴄᴍᴅ ᴛᴏ ᴅɪsᴄᴏɴɴᴇᴄᴛ ʏᴏᴜʀ Aɴɪʟɪsᴛ ᴀᴄᴄᴏᴜɴᴛ/
Usᴇ /me ᴏʀ !me ᴄᴍᴅ ᴛᴏ ɢᴇᴛ ʏᴏᴜʀ ᴀɴɪʟɪsᴛ ʀᴇᴄᴇɴᴛ ᴀᴄᴛɪᴠɪᴛʏ.
Cᴀɴ ᴀʟsᴏ ᴜsᴇ /activity ᴏʀ !activity.
Usᴇ /favourites ᴏʀ !favourites ᴄᴍᴅ ᴛᴏ ɢᴇᴛ ʏᴏᴜʀ ᴀɴɪʟɪsᴛ ғᴀᴠᴏᴜʀɪᴛᴇs.**

"""
