import asyncio
import threading
from aiohttp import web
from pyrogram import Client

# --- Dummy Webserver for Koyeb health check ---
async def handle(request):
    return web.Response(text="Bot is running on Koyeb!")

def run_web():
    app = web.Application()
    app.router.add_get("/", handle)
    web.run_app(app, port=8000)

# Start the webserver in a background thread
threading.Thread(target=run_web, daemon=True).start()

# --- Your Bot ---
API_ID = int("YOUR_API_ID")
API_HASH = "YOUR_API_HASH"
BOT_TOKEN = "YOUR_BOT_TOKEN"

Banword = Client(
    "Banword",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

async def roy_bot():
    async with Banword:
        await Banword.send_message("me", "✅ Bot started successfully on Koyeb!")

if __name__ == "__main__":
    asyncio.run(roy_bot())
