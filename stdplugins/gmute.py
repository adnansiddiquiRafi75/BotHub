from telethon import events
import asyncio
from uniborg.util import admin_cmd


@borg.on(admin_cmd("gmute ?(.*)"))
async def _(event):
    if event.fwd_from:
        return
    reason = event.pattern_match.group(1)
    if event.reply_to_msg_id:
        r = await event.get_reply_message()
        if r.forward:
            r_from_id = r.forward.from_id or r.from_id
        else:
            r_from_id = r.from_id
        await borg.send_message(
            Config.G_MUTE_LOGGER_GROUP,
            "!gban [user](tg://user?id={}) {}".format(r_from_id, reason)
        )
    await event.delete()


@borg.on(admin_cmd("ungmute ?(.*)"))
async def _(event):
    if event.fwd_from:
        return
    reason = event.pattern_match.group(1)
    if event.reply_to_msg_id:
        r = await event.get_reply_message()
        r_from_id = r.from_id
        await borg.send_message(
            Config.G_MUTE_LOGGER_GROUP,
            "!ungmute [user](tg://user?id={}) {}".format(r_from_id, reason)
        )
    await event.delete()
