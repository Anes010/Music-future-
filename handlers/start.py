import asyncio

from helpers.filters import command
from config import BOT_NAME as bn, BOT_USERNAME as bu, SUPPORT_GROUP, OWNER_USERNAME as me, START_IMG
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton


@Client.on_message(command("start") & filters.private & ~filters.group & ~filters.edited)
async def start_(client: Client, message: Message):
    await message.delete()
    await message.reply_sticker("CAACAgUAAxkBAAEENxZiNtPdibVkMsjLZrUG9NK4hotHQgAC2wEAAoM12VSdN9ujxVtnUyME")
    await message.reply_photo(
        photo=f"{START_IMG}",
        caption=f"""**━━━━━━━━━━━━━━━━━━
 ʜᴇʏ {message.from_user.mention()} !

        هذا [{bn}](t.me/{bu}), اسرع بوت مشغل اغاني لاتصال كروبات التلي...

جميع هذه الرموز يمكنك استخدامها لتشيغيلي: ( `/ . • $ ^ ~ + * ?` )

★
★ مطور البوت: [ANES](t.me/{me})
★ قناه البوت:  (t.me/{chanel_bot})


اذا واجهك اي مشكله كل الي عليك تراسل [المطور](t.me/{me}) عزيزي...
━━━━━━━━━━━━━━━━━━**""",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "اضفني الى المجموعه عزيزي", url=f"https://t.me/{bu}?startgroup=true"
                       ),
                  ],[
                    InlineKeyboardButton(
                        "المطور", url=f"https://t.me/{me}"
                    ),
                    InlineKeyboardButton(
                        "ابلاغ", url=f"https://t.me/{SUPPORT_GROUP}"
                    )
                ],[
                    InlineKeyboardButton(
                        " ɪɴʟɪɴᴇ ", switch_inline_query_current_chat=""
                    ),
                    InlineKeyboardButton(
                        "السورس", url="https://github.com/Anes010/Music-future-"
                    )]
            ]
       ),
    )

