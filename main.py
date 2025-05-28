import asyncio
from telegram import Bot

BOT_TOKEN = "YOUR_BOT_TOKEN"
CHANNEL_ID = "-100XXXXXXXXXX"  # Replace this with your real channel ID

async def send_signal():
    bot = Bot(token=BOT_TOKEN)
    await bot.send_message(chat_id=CHANNEL_ID, text="🚀 Hedge Pulse Bot Activated!")

asyncio.run(send_signal())
