# Ayra - UserBot
# Copyright (C) 2021-2022 senpai80
#
# This file is a part of < https://github.com/senpai80/Ayra/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/senpai80/Ayra/blob/main/LICENSE/>.

"""
◈ Perintah Tersedia -

• `{i}mt`
   Mute playback.

• `{i}unmt`
   UnMute playback.

• `{i}ps`
   Pause playback.

• `{i}rs`
   Resume playback.

• `{i}rp`
   Re-play the current song from the beginning.
"""
from . import vc_asst, Player, get_string


@vc_asst("(mutevc|mt)")
async def mute(event):
    if len(event.text.split()) > 1:
        chat = event.text.split()[1]
        try:
            chat = await event.client.parse_id(chat)
        except Exception as e:
            return await event.eor(f"**ERROR:**\n{str(e)}")
    else:
        chat = event.chat_id
    aySongs = Player(chat)
    await aySongs.group_call.set_is_mute(True)
    await event.eor(get_string("vcbot_12"))


@vc_asst("(unmutevc|unmt)")
async def unmute(event):
    if len(event.text.split()) > 1:
        chat = event.text.split()[1]
        try:
            chat = await event.client.parse_id(chat)
        except Exception as e:
            return await event.eor(f"**ERROR:**\n{str(e)}")
    else:
        chat = event.chat_id
    aySongs = Player(chat)
    await aySongs.group_call.set_is_mute(False)
    await event.eor("`Menyalakan pemutaran di obrolan ini.`")


@vc_asst("(pausevc|ps)")
async def pauser(event):
    if len(event.text.split()) > 1:
        chat = event.text.split()[1]
        try:
            chat = await event.client.parse_id(chat)
        except Exception as e:
            return await event.eor(f"**ERROR:**\n{str(e)}")
    else:
        chat = event.chat_id
    aySongs = Player(chat)
    await aySongs.group_call.set_pause(True)
    await event.eor(get_string("vcbot_14"))


@vc_asst("(resumevc|rs)")
async def resumer(event):
    if len(event.text.split()) > 1:
        chat = event.text.split()[1]
        try:
            chat = await event.client.parse_id(chat)
        except Exception as e:
            return await event.eor(f"**ERROR:**\n{str(e)}")
    else:
        chat = event.chat_id
    aySongs = Player(chat)
    await aySongs.group_call.set_pause(False)
    await event.eor(get_string("vcbot_13"))


@vc_asst("replay")
async def replayer(event):
    if len(event.text.split()) > 1:
        chat = event.text.split()[1]
        try:
            chat = await event.client.parse_id(chat)
        except Exception as e:
            return await event.eor(f"**ERROR:**\n{str(e)}")
    else:
        chat = event.chat_id
    aySongs = Player(chat)
    aySongs.group_call.restart_playout()
    await event.eor("`Memutar ulang lagu saat ini.`")
