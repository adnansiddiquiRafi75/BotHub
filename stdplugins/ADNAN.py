"""Emoji
Available Commands:
.ADNAN"""

from telethon import events

import asyncio





@borg.on(events.NewMessage(pattern=r"\.(.*)", outgoing=True))

async def _(event):

    if event.fwd_from:

        return

    animation_interval = 0.3

    animation_ttl = range(0, 31)

    input_str = event.pattern_match.group(1)

    if input_str == "ADNAN":

        await event.edit(input_str)

        animation_chars = [

            "̴A̴̴D̴N̋AN̋A̴̴D̴N̋AN̴̋A̴̴D̴N̋AN̴̋A̴̴D̴N̋AN̋\n̴A̴̴D̴N̋AN̴̋A̴̴D̴N̋AN̴̋A̴̴D̴N̋AN̴̋A̴̴D̴N̋AN̴̋A̴̴D̴N̋AN̋\n̴A̴̴D̴N̋AN̴̋A̴̴D̴N̋AN̴̋A̴̴D̴N̋AN̴̋A̴̴D̴N̋AN̴̋A̴̴D̴N̋AN̋\n̴A̴̴D̴N̋AN̴̋A̴̴D̴N̋AN̴̋A̴̴D̴N̋AN̴̋A̴̴D̴N̋AN̴̋A̴̴D̴N̋AN̋\n̴A̴̴D̴N̋AN̴̋A̴̴D̴N̋AN̴̋A̴̴D̴N̋AN̴̋A̴̴D̴N̋AN̴̋A̴̴D̴N̋AN̋",

            "◼️̴A̴̴D̴N̋AN̴̋A̴̴D̴N̋AN̴̋A̴̴D̴N̋AN̴̋A̴̴D̴N̋AN̋\n̴A̴̴D̴N̋AN̴̋A̴̴D̴N̋AN̴̋A̴̴D̴N̋AN̴̋A̴̴D̴N̋AN̴̋A̴̴D̴N̋AN̋\n̴A̴̴D̴N̋AN̴̋A̴̴D̴N̋AN̴̋A̴̴D̴N̋AN̴̋A̴̴D̴N̋AN̴̋A̴̴D̴N̋AN̋\n̴A̴̴D̴N̋AN̴̋A̴̴D̴N̋AN̴̋A̴̴D̴N̋AN̴̋A̴̴D̴N̋AN̴̋A̴̴D̴N̋AN̋\n̴A̴̴D̴N̋AN̴̋A̴̴D̴N̋AN̴̋A̴̴D̴N̋AN̴̋A̴̴D̴N̋AN̴̋A̴̴D̴N̋AN̋",

            "◼️◼️̴A̴̴D̴N̋AN̴̋A̴̴D̴N̋AN̴̋A̴̴D̴N̋AN̋\n̴A̴̴D̴N̋AN̴̋A̴̴D̴N̋AN̴̋A̴̴D̴N̋AN̴̋A̴̴D̴N̋AN̴̋A̴̴D̴N̋AN̋\n̴A̴̴D̴N̋AN̴̋A̴̴D̴N̋AN̴̋A̴̴D̴N̋AN̴̋A̴̴D̴N̋AN̴̋A̴̴D̴N̋AN̋\n̴A̴̴D̴N̋AN̴̋A̴̴D̴N̋AN̴̋A̴̴D̴N̋AN̴̋A̴̴D̴N̋AN̴̋A̴̴D̴N̋AN̋\n̴A̴̴D̴N̋AN̴̋A̴̴D̴N̋AN̴̋A̴̴D̴N̋AN̴̋A̴̴D̴N̋AN̴̋A̴̴D̴N̋AN̋",

            "◼️◼️◼️️̴A̴̴D̴N̋AN̴̋A̴̴D̴N̋AN̋\n̴A̴̴D̴N̋AN̴̋A̴̴D̴N̋AN̴̋A̴̴D̴N̋AN̴̋A̴̴D̴N̋AN̴̋A̴̴D̴N̋AN̋\n̴A̴̴D̴N̋AN̴̋A̴̴D̴N̋AN̴̋A̴̴D̴N̋AN̴̋A̴̴D̴N̋AN̴̋A̴̴D̴N̋AN̋\n̴A̴̴D̴N̋AN̴̋A̴̴D̴N̋AN̴̋A̴̴D̴N̋AN̴̋A̴̴D̴N̋AN̴̋A̴̴D̴N̋AN̋\n̴A̴̴D̴N̋AN̴̋A̴̴D̴N̋AN̴̋A̴̴D̴N̋AN̴̋A̴̴D̴N̋AN̴̋A̴̴D̴N̋AN̋",

            "◼️◼️◼️◼️̴A̴̴D̴N̋AN̋\n̴A̴̴D̴N̋AN̴̋A̴̴D̴N̋AN̴̋A̴̴D̴N̋AN̴̋A̴̴D̴N̋AN̴̋A̴̴D̴N̋AN̋\n̴A̴̴D̴N̋AN̴̋A̴̴D̴N̋AN̴̋A̴̴D̴N̋AN̴̋A̴̴D̴N̋AN̴̋A̴̴D̴N̋AN̋\n̴A̴̴D̴N̋AN̴̋A̴̴D̴N̋AN̴̋A̴̴D̴N̋AN̴̋A̴̴D̴N̋AN̴̋A̴̴D̴N̋AN̋\n̴A̴̴D̴N̋AN̴̋A̴̴D̴N̋AN̴̋A̴̴D̴N̋AN̴̋A̴̴D̴N̋AN̴̋A̴̴D̴N̋AN̋",

            "‎◼️◼️◼️◼️◼️\n̴A̴̴D̴N̋AN̴̋A̴̴D̴N̋AN̴̋A̴̴D̴N̋AN̴̋A̴̴D̴N̋AN̴̋A̴̴D̴N̋AN̋\n̴A̴̴D̴N̋AN̴̋A̴̴D̴N̋AN̴̋A̴̴D̴N̋AN̴̋A̴̴D̴N̋AN̴̋A̴̴D̴N̋AN̋\n̴A̴̴D̴N̋AN̴̋A̴̴D̴N̋AN̴̋A̴̴D̴N̋AN̴̋A̴̴D̴N̋AN̴̋A̴̴D̴N̋AN̋\n̴A̴̴D̴N̋AN̴̋A̴̴D̴N̋AN̴̋A̴̴D̴N̋AN̴̋A̴̴D̴N̋AN̴̋A̴̴D̴N̋AN̋",

            "◼️◼️◼️◼️◼️\n̴A̴̴D̴N̋AN̴̋A̴̴D̴N̋AN̴̋A̴̴D̴N̋AN̴̋A̴̴D̴N̋AN̋◼️\n̴A̴̴D̴N̋AN̴̋A̴̴D̴N̋AN̴̋A̴̴D̴N̋AN̴̋A̴̴D̴N̋AN̴̋A̴̴D̴N̋AN̋\n̴A̴̴D̴N̋AN̴̋A̴̴D̴N̋AN̴̋A̴̴D̴N̋AN̴̋A̴̴D̴N̋AN̴̋A̴̴D̴N̋AN̋\n̴A̴̴D̴N̋AN̴̋A̴̴D̴N̋AN̴̋A̴̴D̴N̋AN̴̋A̴̴D̴N̋AN̴̋A̴̴D̴N̋AN̋",

            "◼️◼️◼️◼️◼️\n̴A̴̴D̴N̋AN̴̋A̴̴D̴N̋AN̴̋A̴̴D̴N̋AN̴̋A̴̴D̴N̋AN̋◼️\n̴A̴̴D̴N̋AN̴̋A̴̴D̴N̋AN̴̋A̴̴D̴N̋AN̴̋A̴̴D̴N̋AN̋◼️\n̴A̴̴D̴N̋AN̴̋A̴̴D̴N̋AN̴̋A̴̴D̴N̋AN̴̋A̴̴D̴N̋AN̴̋A̴̴D̴N̋AN̋\n̴A̴̴D̴N̋AN̴̋A̴̴D̴N̋AN̴̋A̴̴D̴N̋AN̴̋A̴̴D̴N̋AN̴̋A̴̴D̴N̋AN̋",

            "◼️◼️◼️◼️◼️\n̴A̴̴D̴N̋AN̴̋A̴̴D̴N̋AN̴̋A̴̴D̴N̋AN̴̋A̴̴D̴N̋AN̋◼️\n̴A̴̴D̴N̋AN̴̋A̴̴D̴N̋AN̴̋A̴̴D̴N̋AN̴̋A̴̴D̴N̋AN̋◼️\n̴A̴̴D̴N̋AN̴̋A̴̴D̴N̋AN̴̋A̴̴D̴N̋AN̴̋A̴̴D̴N̋AN̋◼️\n̴A̴̴D̴N̋AN̴̋A̴̴D̴N̋AN̴̋A̴̴D̴N̋AN̴̋A̴̴D̴N̋AN̴̋A̴̴D̴N̋AN̋",

            "◼️◼️◼️◼️◼️\n̴A̴̴D̴N̋AN̴̋A̴̴D̴N̋AN̴̋A̴̴D̴N̋AN̴̋A̴̴D̴N̋AN̋◼️\n̴A̴̴D̴N̋AN̴̋A̴̴D̴N̋AN̴̋A̴̴D̴N̋AN̴̋A̴̴D̴N̋AN̋◼️\n̴A̴̴D̴N̋AN̴̋A̴̴D̴N̋AN̴̋A̴̴D̴N̋AN̴̋A̴̴D̴N̋AN̋◼️\n̴A̴̴D̴N̋AN̴̋A̴̴D̴N̋AN̴̋A̴̴D̴N̋AN̴̋A̴̴D̴N̋AN̋◼️",

            "◼️◼️◼️◼️◼️\n̴A̴̴D̴N̋AN̴̋A̴̴D̴N̋AN̴̋A̴̴D̴N̋AN̴̋A̴̴D̴N̋AN̋◼️\n̴A̴̴D̴N̋AN̴̋A̴̴D̴N̋AN̴̋A̴̴D̴N̋AN̴̋A̴̴D̴N̋AN̋◼️\n̴A̴̴D̴N̋AN̴̋A̴̴D̴N̋AN̴̋A̴̴D̴N̋AN̴̋A̴̴D̴N̋AN̋◼️\n̴A̴̴D̴N̋AN̴̋A̴̴D̴N̋AN̴̋A̴̴D̴N̋AN̋◼️◼️",

            "◼️◼️◼️◼️◼️\n̴A̴̴D̴N̋AN̴̋A̴̴D̴N̋AN̴̋A̴̴D̴N̋AN̴̋A̴̴D̴N̋AN̋◼️\n̴A̴̴D̴N̋AN̴̋A̴̴D̴N̋AN̴̋A̴̴D̴N̋AN̴̋A̴̴D̴N̋AN̋◼️\n̴A̴̴D̴N̋AN̴̋A̴̴D̴N̋AN̴̋A̴̴D̴N̋AN̴̋A̴̴D̴N̋AN̋◼️\n̴A̴̴D̴N̋AN̴̋A̴̴D̴N̋AN̋◼️◼️◼️",

            "◼️◼️◼️◼️◼️\n̴A̴̴D̴N̋AN̴̋A̴̴D̴N̋AN̴̋A̴̴D̴N̋AN̴̋A̴̴D̴N̋AN̋◼️\n̴A̴̴D̴N̋AN̴̋A̴̴D̴N̋AN̴̋A̴̴D̴N̋AN̴̋A̴̴D̴N̋AN̋◼️\n̴A̴̴D̴N̋AN̴̋A̴̴D̴N̋AN̴̋A̴̴D̴N̋AN̴̋A̴̴D̴N̋AN̋◼️\n̴A̴̴D̴N̋AN̋◼️◼️◼️◼️",

            "◼️◼️◼️◼️◼️\n̴A̴̴D̴N̋AN̴̋A̴̴D̴N̋AN̴̋A̴̴D̴N̋AN̴̋A̴̴D̴N̋AN̋◼️\n̴A̴̴D̴N̋AN̴̋A̴̴D̴N̋AN̴̋A̴̴D̴N̋AN̴̋A̴̴D̴N̋AN̋◼️\n̴A̴̴D̴N̋AN̴̋A̴̴D̴N̋AN̴̋A̴̴D̴N̋AN̴̋A̴̴D̴N̋AN̋◼️\n◼️◼️◼️◼️◼️",

            "◼️◼️◼️◼️◼️\n̴A̴̴D̴N̋AN̴̋A̴̴D̴N̋AN̴̋A̴̴D̴N̋AN̴̋A̴̴D̴N̋AN̋◼️\n̴A̴̴D̴N̋AN̴̋A̴̴D̴N̋AN̴̋A̴̴D̴N̋AN̴̋A̴̴D̴N̋AN̋◼️\n◼️̴A̴̴D̴N̋AN̴̋A̴̴D̴N̋AN̴̋A̴̴D̴N̋AN̋◼️\n◼️◼️◼️◼️◼️",

            "◼️◼️◼️◼️◼️\n̴A̴̴D̴N̋AN̴̋A̴̴D̴N̋AN̴̋A̴̴D̴N̋AN̴̋A̴̴D̴N̋AN̋◼️\n◼️̴A̴̴D̴N̋AN̴̋A̴̴D̴N̋AN̴̋A̴̴D̴N̋AN̋◼️\n◼️̴A̴̴D̴N̋AN̴̋A̴̴D̴N̋AN̴̋A̴̴D̴N̋AN̋◼️\n◼️◼️◼️◼️◼️",

            "◼️◼️◼️◼️◼️\n◼️̴A̴̴D̴N̋AN̴̋A̴̴D̴N̋AN̴̋A̴̴D̴N̋AN̋◼️\n◼️̴A̴̴D̴N̋AN̴̋A̴̴D̴N̋AN̴̋A̴̴D̴N̋AN̋◼️\n◼️̴A̴̴D̴N̋AN̴̋A̴̴D̴N̋AN̴̋A̴̴D̴N̋AN̋◼️\n◼️◼️◼️◼️◼️",

            "◼️◼️◼️◼️◼️\n◼️◼️̴A̴̴D̴N̋AN̴̋A̴̴D̴N̋AN̋◼️\n◼️̴A̴̴D̴N̋AN̴̋A̴̴D̴N̋AN̴̋A̴̴D̴N̋AN̋◼️\n◼️̴A̴̴D̴N̋AN̴̋A̴̴D̴N̋AN̴̋A̴̴D̴N̋AN̋◼️\n◼️◼️◼️◼️◼️",

            "◼️◼️◼️◼️◼️\n◼️◼️◼️̴A̴̴D̴N̋AN̋◼️\n◼️̴A̴̴D̴N̋AN̴̋A̴̴D̴N̋AN̴̋A̴̴D̴N̋AN̋◼️\n◼️̴A̴̴D̴N̋AN̴̋A̴̴D̴N̋AN̴̋A̴̴D̴N̋AN̋◼️\n◼️◼️◼️◼️◼️",

            "◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️̴A̴̴D̴N̋AN̴̋A̴̴D̴N̋AN̴̋A̴̴D̴N̋AN̋◼️\n◼️̴A̴̴D̴N̋AN̴̋A̴̴D̴N̋AN̴̋A̴̴D̴N̋AN̋◼️\n◼️◼️◼️◼️◼️",

            "◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️̴A̴̴D̴N̋AN̴̋A̴̴D̴N̋AN̋◼️◼️\n◼️̴A̴̴D̴N̋AN̴̋A̴̴D̴N̋AN̴̋A̴̴D̴N̋AN̋◼️\n◼️◼️◼️◼️◼️",

            "◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️̴A̴̴D̴N̋AN̴̋A̴̴D̴N̋AN̋◼️◼️\n◼️̴A̴̴D̴N̋AN̴̋A̴̴D̴N̋AN̋◼️◼️\n◼️◼️◼️◼️◼️",

            "◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️̴A̴̴D̴N̋AN̴̋A̴̴D̴N̋AN̋◼️◼️\n◼️̴A̴̴D̴N̋AN̋◼️◼️◼️\n◼️◼️◼️◼️◼️",

            "◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️̴A̴̴D̴N̋AN̴̋A̴̴D̴N̋AN̋◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️",

            "◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️̴A̴̴D̴N̋AN̋◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️",

            "◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️",

            "◼️◼️◼️◼️\n◼️◼️◼️◼️\n◼️◼️◼️◼️\n◼️◼️◼️◼️",

            "◼️◼️◼️\n◼️◼️◼️\n◼️◼️◼️",

            "◼️◼️\n◼️◼️",

            "◼️",
            
            "A̴̴D̴N̋AN̋"
        ]

        for i in animation_ttl:

            await asyncio.sleep(animation_interval)

            await event.edit(animation_chars[i % 31])
