import os

from pyrogram import Client, filters
from pyrogram.types import Message


SESSION = "AgDFycsATXUek6C8lXsCVfirGHeZHeiouRE7-ASlZD5bzCnt_U_Hpa9tWe1x_WceG6RixoVzZ5q-7NqMqpiR3wZtoSR8_Rz7qricCWcFlaZBPvahHkHKpAvHI9ePjadOX7vvRxEJkoOACsUkHNHhTcipQ6XZW_42la6mG4bTO_XJx80IFHrM3L29SzMkslfiZUyuE9g42z-m4qSxwTADrtLT-NmqJ35Kf7Xt8pcm0NYnlAC4yfK6kXs_GrpUqGDDoPacgGJf4OSVB0MRtVQKKw8qnYpIkuA9wpUGZjhImr2ilOSfQCkMgVS85-ig4FQ--gMGSdocsf0eqmbH1iH1iIGWk3C-gQAAAAAxrBH9AA" # pyrogram string session 
API_ID = 12962251 # Your API_ID Get it from my.telegram.org
API_HASH = "b51499523800add51e4530c6f552dbc8" # Your API_HASH Get it from my.telegram.org

app = Client(
      'session_name',
      API_ID, API_HASH, session_string = SESSION, #in_memory=True
)

@app.on_message(filters.self_destruction, group=6)
async def save_timer_media(client: Client, message: Message):
    try:
        if message.media:
            file_path = await message.download()
            await client.send_document(
                "me", document=file_path, caption=message.caption or "Saved timer media"
            )
            os.remove(file_path)
    except Exception as e:
        print(f"Error: {e}")


# Command to save a specific photo timer message
@app.on_message(
    filters.command(["save", "سەیڤ", "/save"], "") & filters.reply, group=7
)
async def save_replied_timer_photo(client: Client, message: Message):
    try:
        # Ensure the replied message has a media file
        if message.reply_to_message and message.reply_to_message.media:
            file_path = await message.reply_to_message.download()
            await client.send_document(
                "me",
                document=file_path,
                caption=message.reply_to_message.caption or "Saved replied timer photo",
            )
            os.remove(file_path)
            await message.reply("اوفف")
        else:
            await message.reply("Please reply to a timer photo message to save it.")
    except Exception as e:
        print(f"Error: {e}")
        await message.reply("Failed to save the timer photo.")
        
        
        
app.run()
