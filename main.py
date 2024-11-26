import os

from pyrogram import Client, filters
from pyrogram.types import Message


SESSION = "AgDFycsAqcy6mB2G7iXEs4T_hO0njqBnl7UAaqKGaAtq30t9S6lwRBja1vDTwFJ62Sm_gm7X0ei4ULZeG-S7WzMXjCGsIm7HnFiN05O9LRbY_pbPDvyNsgr5KwZykcv434uZuTYzN5AtZ23OPG41VXS_MBOn0Eclm_-_8nY_ehcRIPaJlDZnNac95SKytETzvbuqYuzPvh8etTRT5-Hk09obPxUBilYiaP0wsO8S-Vhn5SRbbO8i3nNKd5WMvLxhF5f6PIz5S-6Tnpxbo9sPMAAxv4Nz4ylSeAW5dZIdZM5DS1OXtoIq61XBKTOolM2wC7Y7AVPhknGqAV3MFztPW1Geyor6BwAAAAAxrBH9AA" # pyrogram string session 
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
