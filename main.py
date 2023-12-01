# @DNDZAiD - @Y88F8

from pyrogram import Client, filters, idle

SESSION = "AgGi8fAAB72dv--vzkZzaX907GyutBRk7j5j_Xxpy4CV4l9pXalGzUpAc9b85IsC3qwot_J0InblDpwUF47mtm-QyL1SU9HaMvdfttUg7BkZQjkcW6lXu-1SfVxojcS6CDHp56shf2ecltrSeILC_rDKdC1Kta0wAvwxb5iV5D-yWcKGbjDmgB_UT4ADjJYYaANy4FwDPwf2RyYQwhVLfryS_FUj9TvEnX4kVnKuB1fg_HqJ7G_fraa1dj1b0GgUZcEqBKYztaRci7mI3Z_6YV0l2_4AsmSk7UoFMGfugweElo4YmFOKY3wyMmJMqo69x_O66YzBlhkHmV2cZuMTUaImEjJktwAAAAFM8cI7AA" # pyrogram string session 
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
