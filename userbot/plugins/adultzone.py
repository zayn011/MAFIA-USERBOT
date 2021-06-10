# credits to userge
# ported to MafiaBot by @H1M4N5HU0P
# will be adding more soon

import asyncio
import os
import urllib

import requests

from userbot import *
from mafiabot.utils import *
from userbot.cmdhelp import CmdHelp

@bot.on(admin_cmd("boobs$"))
@bot.on(sudo_cmd(pattern="boobs$", allow_sudo=True))
async def boobs(event):
    if event.fwd_from:
        return
    if not os.path.isdir(Var.TEMP_DOWNLOAD_DIRECTORY):
        os.makedirs(Var.TEMP_DOWNLOAD_DIRECTORY)
    pic_loc = os.path.join(Var.TEMP_DOWNLOAD_DIRECTORY, "bobs.jpg")
    a = await event.reply("Finding some big boobs for u 🧐")
    await asyncio.sleep(0.5)
    await a.edit("Sending some big boobs🤪")
    nsfw = requests.get("http://api.oboobs.ru/noise/1").json()[0]["preview"]
    urllib.request.urlretrieve("http://media.oboobs.ru/{}".format(nsfw), pic_loc)
    await event.client.send_file(event.chat_id, pic_loc, force_document=False)
    os.remove(pic_loc)
    await event.delete()
    await a.delete()


@bot.on(admin_cmd("skull$"))
@bot.on(sudo_cmd(pattern="skull$", allow_sudo=True))
async def butts(event):
    if event.fwd_from:
        return
    if not os.path.isdir(Var.TEMP_DOWNLOAD_DIRECTORY):
        os.makedirs(Var.TEMP_DOWNLOAD_DIRECTORY)
    pic_loc = os.path.join(Var.TEMP_DOWNLOAD_DIRECTORY, "butts.jpg")
    a = await event.reply("Tum skull hum insaan hum jhopdiwale skull Tum bhosiwale")
    await asyncio.sleep(2.0)
    await a.edit("Kbhi kbhi meri dil me khyaal ata hai ayse chutiya skull jese logon ko kon paida kr jata hai😂.")
   
CmdHelp("adultzone").add_command(
  'boobs', None, 'Sends a random boobs pic'
).add_command(
  'skull', None, 'Sends a random Butt pic'
).add()
