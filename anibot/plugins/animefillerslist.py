from pyrogram import filters
from pyrogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    CallbackQuery,
    Message
)
from ..utils.data_parser import search_filler, parse_filler
from ..utils.helper import (
    check_user,
    control_user,
    rand_key,
    get_user_from_channel as gcc
)
from ..utils.db import get_collection
from .. import BOT_NAME, TRIGGERS as trg, anibot

FILLERS = {}
DC = get_collection('DISABLED_CMDS')


@anibot.on_message(
    filters.command(['fillers', f"fillers{BOT_NAME}"], prefixes=trg)
)
@control_user
async def fillers_cmd(client: anibot, message: Message, mdata: dict):
    find_gc = await DC.find_one({'_id': mdata['chat']['id']})
    try:
        user = mdata['from_user']['id']
    except KeyError:
        user = mdata['sender_chat']['id']
    if find_gc is not None and 'watch' in find_gc['cmd_list'].split():
        return
    qry = mdata['text'].split(" ", 1)
    if len(qry)==1:
        return await message.reply_text(
"""Gɪᴠᴇ sᴏᴍᴇ ᴀɴɪᴍᴇ ɴᴀᴍᴇ ᴛᴏ sᴇᴀʀᴄʜ ғɪʟʟᴇʀs ғᴏʀ
ᴇxᴀᴍᴘʟᴇ: /fillers Detective Conan"""
        )
    k = search_filler(qry[1])
    if k == {}:
        await message.reply_text("Nᴏ ғɪʟʟᴇʀs ғᴏᴜɴᴅ ғᴏʀ ᴛʜᴇ ɢɪᴠᴇɴ ᴀɴɪᴍᴇ...")
        return
    button = []
    list_ = list(k.keys())
    if len(list_)==1:
        result = parse_filler(k.get(list_[0]))
        msg = ""
        msg += f"Fɪʟʟᴇʀs ғᴏʀ ᴀɴɪᴍᴇ `{list_[0]}`\n\nMᴀɴɢᴀ Cᴀɴᴏɴ ᴇᴘɪsᴏᴅᴇs:\n"
        msg += str(result.get("total_ep"))
        msg += "\n\nMɪxᴇᴅ/Cᴀɴᴏɴ ғɪʟʟᴇʀs:\n"
        msg += str(result.get("mixed_ep"))
        msg += "\n\nFɪʟʟᴇʀs:\n"
        msg += str(result.get("filler_ep"))
        if result.get("ac_ep") is not None:
            msg += "\n\nAɴɪᴍᴇ Cᴀɴᴏɴ ᴇᴘɪsᴏᴅᴇs:\n"
            msg += str(result.get("ac_ep"))
        await message.reply_text(msg)
        return
    for i in list_:
        fl_js = rand_key()
        FILLERS[fl_js] = [k.get(i), i]
        button.append(
            [InlineKeyboardButton(i, callback_data=f"fill_{fl_js}_{user}")]
        )
    await message.reply_text(
        "Pɪᴄᴋ ᴀɴɪᴍᴇ ʏᴏᴜ ᴡᴀɴᴛ ᴛᴏ sᴇᴇ ғɪʟʟᴇʀs ʟɪsᴛ ғᴏʀ:",
        reply_markup=InlineKeyboardMarkup(button)
    )


@anibot.on_callback_query(filters.regex(pattern=r"fill_(.*)"))
@check_user
async def filler_btn(client: anibot, cq: CallbackQuery, cdata: dict):
    kek, req, user = cdata['data'].split("_")
    result = parse_filler((FILLERS.get(req))[0])
    msg = ""
    msg += f"**Fɪʟʟᴇʀs ғᴏʀ ᴀɴɪᴍᴇ** `{(FILLERS.get(req))[1]}`"
    msg += "\n\n**Mᴀɴɢᴀ Cᴀɴᴏɴ ᴇᴘɪsᴏᴅᴇs:**\n"
    msg += str(result.get("total_ep"))
    msg += "\n\n**Mɪxᴇᴅ/Cᴀɴᴏɴ ғɪʟʟᴇʀs:**\n"
    msg += str(result.get("mixed_ep"))
    msg += "\n\n**Fɪʟʟᴇʀs:**\n"
    msg += str(result.get("filler_ep"))
    if result.get("ac_ep") is not None:
        msg += "\n\n**Aɴɪᴍᴇ Cᴀɴᴏɴ ᴇᴘɪsᴏᴅᴇs:**\n"
        msg += str(result.get("ac_ep"))
    await cq.edit_message_text(msg)


@anibot.on_message(
    filters.command(['fillers', f"fillers{BOT_NAME}"], prefixes=trg)
)
async def fillers_cmd(client: anibot, message: Message):
    await fillers_cmd(client, message)
