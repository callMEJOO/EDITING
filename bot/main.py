# main.py

import asyncio
import logging

from aiogram import Bot, Dispatcher

from config import TOKEN

# routers
from start import router as start_router
from video import router as video_router
from admin import router as admin_router
from callbacks import router as callbacks_router


# ==================================
# Logging
# ==================================
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
)


# ==================================
# Main Function
# ==================================
async def main():
    bot = Bot(token=TOKEN)
    dp = Dispatcher()

    # تسجيل الراوترات
    dp.include_router(start_router)
    dp.include_router(video_router)
    dp.include_router(admin_router)
    dp.include_router(callbacks_router)

    logging.info("Bot Started Successfully")

    await dp.start_polling(bot)


# ==================================
# Start App
# ==================================
if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Bot Stopped")
