# __main__.py

import asyncio
import os
from pyrogram import Client
from motor.motor_asyncio import AsyncIOMotorClient

# ------------------ Environment Variables ------------------
API_ID = int(os.environ.get("API_ID", "123456"))
API_HASH = os.environ.get("API_HASH", "your_api_hash")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "your_bot_token")
MONGO_URL = os.environ.get("MONGO_URL", "mongodb+srv://sk5400552:shjjkytdcghhudd@cluster0g.kbllv.mongodb.net/banword_db?retryWrites=true&w=majority&appName=Cluster0g")
DB_NAME = os.environ.get("DB_NAME", "banword_db")   # specify your DB name
LOGGER_ID = int(os.environ.get("LOGGER_ID", "0"))
OWNER_ID = int(os.environ.get("OWNER_ID", "0"))
BOT_USERNAME = os.environ.get("BOT_USERNAME", "your_bot_username")

# ------------------ MongoDB Setup ------------------
mongo_client = AsyncIOMotorClient(MONGO_URL)
db = mongo_client.get_database(DB_NAME)  # explicitly set DB

# ------------------ Main Bot ------------------
async def main():
    async with Client(
        "banword_bot",
        api_id=API_ID,
        api_hash=API_HASH,
        bot_token=BOT_TOKEN,
    ) as app:
        print(f"{BOT_USERNAME} started successfully!")

        # Send start message to logger
        try:
            await app.send_message(LOGGER_ID, f"{BOT_USERNAME} has started!")
        except Exception as e:
            print(f"Logger message failed: {e}")

        # Example: Owner ID usage
        print(f"Bot Owner ID: {OWNER_ID}")

        # ------------------ Idle ------------------
        await app.idle()  # keeps bot running

# ------------------ Run ------------------
if __name__ == "__main__":
    asyncio.run(main())
