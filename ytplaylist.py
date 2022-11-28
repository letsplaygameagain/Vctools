# Ayra - UserBot
# Copyright (C) 2021-2022 senpai80
#
# This file is a part of < https://github.com/senpai80/Ayra/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/senpai80/Ayra/blob/main/LICENSE/>.

"""
◈ Perintah Tersedia -

`{i}ytplaylist <playlist link>`
  play whole playlist in voice chat

"""

import re
from . import vc_asst, get_string, inline_mention, Player, dl_playlist, add_to_queue, is_url_ok, VC_QUEUE


@vc_asst("ytplaylist")
async def live_stream(e):
    xx = await e.eor(get_string("com_1"))
    if len(e.text.split()) <= 1:
        return await xx.eor("Apakah Anda Bercanda?\nYang Harus Dimainkan?")
    input = e.text.split()
    if input[1].startswith("-"):
        chat = int(input[1])
        song = e.text.split(maxsplit=2)[2]
    elif input[1].startswith("@"):
        cid_moosa = (await e.client.get_entity(input[1])).id
        chat = int(f"-100{str(cid_moosa)}")
        song = e.text.split(maxsplit=2)[2]
    else:
        song = e.text.split(maxsplit=1)[1]
        chat = e.chat_id
    if not (re.search("youtu", song) and re.search("playlist\\?list", song)):
        return await xx.eor(get_string("vcbot_8"))
    if not is_url_ok(song):
        return await xx.eor("`Only Youtube Playlist please.`")
    await xx.edit(get_string("vcbot_7"))
    file, thumb, title, link, duration = await dl_playlist(
        chat, inline_mention(e), song
    )
    aySongs = Player(chat, e)
    if not aySongs.group_call.is_connected:
        if not (await aySongs.vc_joiner()):
            return
        from_user = inline_mention(e.sender)
        await xx.reply(
            "🎥 **Sedang dimainkan:** [{}]({})\n⏰ **Durasi:** `{}`\n👥 **Di:** `{}`\n🙋‍♂ **Diminta oleh:** {}".format(
                f"{title[:30]}...", link, duration, chat, from_user
            ),
            file=thumb,
            link_preview=False,
        )

        await xx.delete()
        await aySongs.group_call.start_audio(file)
    else:
        from_user = inline_mention(e)
        add_to_queue(chat, file, title, link, thumb, from_user, duration)
        return await xx.eor(
            f"✚ Ditambahkan 🎥 **[{title}]({link})** antrian ke #{list(VC_QUEUE[chat].keys())[-1]}.",
        )
