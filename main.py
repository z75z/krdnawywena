# @DNDZAiD - @Y88F8

from pyrogram import Client, filters, idle

SESSION = "AgAhIHQAlKSxKdju-HtHsJl62CvRASw879V3r5n9G5jGdwzJELydKm5Bd5wtxwL4noZR03_tzazlZYGhFRWW_K_-gWKMI_wvOTtoK0kGYbborMS1pK74l82WIkbOC01ZA28_k59kCAyG4MOgkdgImWNJKHG5dVeNfHxZxR0H5UpfwzT7ww8npADxCBzbPDexioJ-zozECfRG1X1pCY7tBXPVC7BhyArFiYiGuEcw4eJ9PiUg9iNQtdIoCVJicK7Su5es-k3LNTS4SxLMYmPDJ3gGXyZhPmQsW2JUn9MinemlbBD4-9S9b2Z9xhQhMcm0kpySNGT-mQRHnt3gZrlEoX607XI3vQAAAAAxrBH9AA" # pyrogram string session 
API_ID = 12962251 # Your API_ID Get it from my.telegram.org
API_HASH = 'b51499523800add51e4530c6f552dbc8' # Your API_HASH Get it from my.telegram.org

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
