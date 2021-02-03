from pyrogram import Client, Filters, StopPropagation, InlineKeyboardButton, InlineKeyboardMarkup


@Client.on_message(Filters.command(["start"]), group=-2)
async def start(client, message):
    # return
    joinButton = InlineKeyboardMarkup([
        [InlineKeyboardButton(
            "Created By 😊", url="https://t.me/abisri99")]
    ])
    welcomed = f"Hey <b>{message.from_user.first_name}</b>\n/"
    await message.reply_text(welcomed, reply_markup=joinButton)
    raise StopPropagation
