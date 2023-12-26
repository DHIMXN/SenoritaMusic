from config import LOG, LOG_GROUP_ID, MUSIC_BOT_NAME
from ShizukaXMusic.utils.database import is_on_off
from ShizukaXMusic import app


async def play_logs(message, streamtype):
    if await is_on_off(LOG):
        if message.chat.username:
            chatusername = f"@{message.chat.username}"
        else:
            chatusername = "Mᴜsɪᴄ Lᴏɢs !! 🗞️"
        logger_text = f"""
**━━━━━━━━━━━━━━━**
**🐼 {MUSIC_BOT_NAME} Mᴜsɪᴄ Lᴏɢs **
**━━━━━━━━━━━━━━━**
**💗 Cʜᴀᴛ Nᴀᴍᴇ : >** {message.chat.title} [`{message.chat.id}`]
**━━━━━━━━━━━━━━━**
**🐼 Nᴀᴍᴇ : ›** {message.from_user.mention}
**━━━━━━━━━━━━━━━**
**💗 Usᴇʀɴᴀᴇ : ›** @{message.from_user.username}
**━━━━━━━━━━━━━━━**
**🐼 Usᴇʀ Iᴅ  : ›** `{message.from_user.id}`
**━━━━━━━━━━━━━━━**
**💗 Cʜᴀᴛ Lɪɴᴋ : >** {chatusername}
**━━━━━━━━━━━━━━━**
**🐼 Sᴇᴀʀᴄʜᴇᴅ Fᴏʀ : >** {message.text}
**━━━━━━━━━━━━━━━**
**💗 Sᴛʀᴇᴀᴍ Tʏᴘᴇ : >** {streamtype}
**━━━━━━━━━━━━━━━**"""
        if message.chat.id != LOG_GROUP_ID:
            try:
                await app.send_message(
                    LOG_GROUP_ID,
                    f"{logger_text}",
                    disable_web_page_preview=True,
                )
            except:
                pass
        return
