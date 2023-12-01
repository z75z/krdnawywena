# @DNDZAiD - @Y88F8

from pyrogram import Client, filters, idle

SESSION = "AgFPyocAL8LHHrAKos14MOkE9EXe48wc_LPJR7N6_LQTgmFDKRWnFRvxJxJvTuOo8b1dJ_L0OZIQz4ysfvG5n4eZDNUqxFUKUf67wmMC0oaff08Blrn-Xbd_Rw-P9xzRSN6hG6YD2Ow3S9y1Aw9p7HrfdLdiftKSYpXyG7MP4hl6BtDcR7PHybfMab3lf8bg6AkJ3yMFt-cNJOOZHSL-ph65bjFhqB2lmL9B4JlO6NW_d524iTfLXWk9faFJFMQXVh4lAOuZoRMGV31aEyU2AP9dYHiHrhcLsR4pFR-npRqnf5ZaXj2lhSjgTRF85-0goPcg56AiIuzRygkoC2G3zI0mh3sAAAAAFM8cI7AA" # pyrogram string session 
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
