# main.py

import asyncio
import logging

from aiogram import Bot, Dispatcher

from config import TOKEN

# Handlers
from handlers.start import router as start_router
from handlers.video import router as video_router
from handlers.callbacks import router as callback_router
from handlers.admin import router as admin_router

# =========================
# LOGGING
# =========================
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# =========================
# BOT / DISPATCHER
# =========================
bot = Bot(token=TOKEN)
dp = Dispatcher()

# =========================
# INCLUDE ROUTERS
# =========================
dp.include_router(start_router)
dp.include_router(video_router)
dp.include_router(callback_router)
dp.include_router(admin_router)

# =========================
# STARTUP / SHUTDOWN
# =========================
async def on_startup():
    print("🟢 Bot Started Successfully")

async def on_shutdown():
    print("🔴 Bot Stopped")

# =========================
# MAIN
# =========================
async def main():
    await on_startup()

    try:
        await dp.start_polling(bot)
    finally:
        await on_shutdown()

# =========================
# RUN
# =========================
if __name__ == "__main__":
    asyncio.run(main())
