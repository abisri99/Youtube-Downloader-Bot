from pyrogram import Client, Filters


@Client.on_message(Filters.command(["btn"]))
async def start(client, message):
    text = message.text.replace("/btn ", "").strip()
    res = "/save "
    temp = text.split("\n")
    res += temp[0]+"\n"
    del temp[0]
    for i in temp:
        foo = i.split(" - ")
        foo[0] = foo[0].strip()
        foo[1] = foo[1].strip()
        res = res + "[" + foo[0] + "](buttonurl://" + foo[1] + ")" + "\n"
    print(res)
    await message.reply_text(res)
