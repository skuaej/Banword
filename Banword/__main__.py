# __main__.py

import asyncio
import os
from pyrogram import Client
from motor.motor_asyncio import AsyncIOMotorClient

# Load environment variables
API_ID = int(os.environ.get("API_ID", "123456"))
API_HASH = os.environ.get("API_HASH", "your_api_hash")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "your_bot_token")
MONGO_URL = os.environ.get("MONGO_URL", "your_mongo_url")
LOGGER_ID = int(os.environ.get("LOGGER_ID", "0"))
OWNER_ID = int(os.environ.get("OWNER_ID", "0"))
BOT_USERNAME = os.environ.get("BOT_USERNAME", "your_bot_username")

# Initialize MongoDB client
mongo_client = AsyncIOMotorClient(MONGO_URL)
db = mongo_client.get_database()  # default DB from URL

async def main():
    async with Client(
        "banword_bot",
        api_id=API_ID,
        api_hash=API_HASH,
        bot_token=BOT_TOKEN,
    ) as app:
        print(f"{BOT_USERNAME} started successfully!")

        # Example: Log bot start in LOGGER_ID
        try:
            await app.send_message(LOGGER_ID, f"{BOT_USERNAME} has started!")
        except Exception as e:
            print(f"Logger message failed: {e}")

        # Example: Owner check usage (you can use OWNER_ID elsewhere in your code)
        print(f"Bot Owner ID: {OWNER_ID}")

        # Keep the bot running
        await app.idle()

if __name__ == "__main__":
    asyncio.run(main())
