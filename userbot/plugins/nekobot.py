# Copyright (c) By Midhun KM [@StarkXD] 
# I Am Noob 
# Official Web : nekobot.xyz
# "Copy It As You Want But Don't Edit Credits"
import requests
from uniborg.util import admin_cmd, sudo_cmd, edit_or_reply

@borg.on(admin_cmd("ttt ?(.*)"))
@borg.on(sudo_cmd("ttt ?(.*)", allow_sudo=True))
async def noobishere(event):
    reply_to_id = event.message.id
    if event.reply_to_msg_id:
        reply_to_id = event.reply_to_msg_id
    reply = await event.get_reply_message()
    if event.pattern_match.group(1):
        ipman = event.pattern_match.group(1)
    elif reply.text:
        ipman = reply.message
    else:
     await edit_or_reply(event.chat_id, "Trump : What Should I Tweet For You ?")
     return
    
    url = f"https://nekobot.xyz/api/imagegen?type=trumptweet&text={ipman}"
    starkgang = requests.get(url=url).json()
    meikobot = starkgang.get("message")
    tweetimg = meikobot
    starkxd = f"Trump Has Tweeted {ipman}"
    await edit_or_reply(event.chat_id, "Trump : Wait I Am Tweeting Your Texts")
    await event.client.send_file(event.chat_id, tweetimg, caption=starkxd, reply_to=reply_to_id) 