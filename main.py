from pyrogram import Client
from config import API_ID, API_HASH, SESSION_NAME
from relay.commands import register

app = Client(
    SESSION_NAME,
    api_id=API_ID,
    api_hash=API_HASH
)

register(app)
print("🔊 VC Relay Bot (Advanced) Started")
app.run()
