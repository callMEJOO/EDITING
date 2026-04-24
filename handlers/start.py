# handlers/start.py

from aiogram import Router
from aiogram.types import Message
from aiogram.filters import CommandStart

from config import START_TEXT
from keyboards.main_menu import main_menu

router = Router()

# ==================================
# /start
# ==================================
@router.message(CommandStart())
async def start_handler(message: Message):
    await message.answer(
        START_TEXT,
        reply_markup=main_menu()
    )

# ==================================
# /help
# ==================================
@router.message(commands=["help"])
async def help_handler(message: Message):
    text = """
📌 أوامر البوت:

/start - تشغيل البوت
/help - المساعدة
/ping - اختبار البوت

🎬 أرسل فيديو ثم اختر الجودة المطلوبة.
"""
    await message.answer(text)

# ==================================
# /ping
# ==================================
@router.message(commands=["ping"])
async def ping_handler(message: Message):
    await message.answer("🏓 Bot is Online")