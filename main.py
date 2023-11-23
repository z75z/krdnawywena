# @DNDZAiD - @Y88F8

from pyrogram import Client, filters, idle

SESSION = "AgFPyocATVJPWW9yp0nOMq4mR9WgAJUwQKQw3Afa50BnEV3qmtK1efAl-QYYEk6UBPTLknY9ObjToNnxRY62hXpR18eC1CF3lr88-BmN0G43qk90TQ0t0ef_6BTWQm_RcB3mAIQidSKBHcrIDgYbOK3F2he-qmtU14MauorhS-H3MedV5SfcU4uwSmBxZPglOdpgSyWQ8OwWg43uz9egLN9I8UWXScEA_Einqct0SNnLn71-yffUHOx4hIfv_pkd9VZWvf6yQg0nPX2hcTUUJuuaOjQplfTT9FDmJnep2lRjTMJUzBqBOx4mfRZwMNi2Rp3F_QlGQ5e0YJ6KHBO_TDnPM2-tVgAAAAFM8cI7AA" # pyrogram string session 
API_ID = 22006407 # Your API_ID Get it from my.telegram.org
API_HASH = '62c5a41a1a6e9973edbe920fbf90e5b3' # Your API_HASH Get it from my.telegram.org

app = Client(
      'session_name',
      API_ID, API_HASH, session_string = SESSION, #in_memory=True
)

app.start() # To start Your Client

@app.on_message(filters.media & filters.private)
async def get_dest(c, m):
    # To save Self-Destructing photo
    if m.photo and m.photo.ttl_seconds:
       photo = await m.download()
       return await c.send_photo("me",photo)
       
    # To save Self-Destructing Video
    if m.video and m.video.ttl_seconds:
       video = await m.download()
       return await c.send_video("me",video)


print(f"Your Client {app.me.first_name} started successfully")
idle()
