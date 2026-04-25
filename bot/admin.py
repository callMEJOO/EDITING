# admin.py

import os

from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command

from config import ADMINS, DOWNLOAD_DIR, OUTPUT_DIR

router = Router()


# ==================================
# التحقق من الأدمن
# ==================================
def is_admin(user_id: int) -> bool:
    return user_id in ADMINS


# ==================================
# /admin
# ==================================
@router.message(Command("admin"))
async def admin_panel(message: Message):
    if not is_admin(message.from_user.id):
        return

    text = """
👑 لوحة الأدمن

الأوامر المتاحة:

/stats - إحصائيات
/users - عدد المستخدمين
/clean - حذف الملفات المؤقتة
/broadcast - إرسال رسالة للجميع (قريبًا)
"""
    await message.answer(text)


# ==================================
# /stats
# ==================================
@router.message(Command("stats"))
async def stats_cmd(message: Message):
    if not is_admin(message.from_user.id):
        return

    downloads = len(os.listdir(DOWNLOAD_DIR))
    outputs = len(os.listdir(OUTPUT_DIR))

    text = f"""
📊 إحصائيات السيرفر

📥 الملفات المستلمة: {downloads}
📤 الملفات المضغوطة: {outputs}
🟢 البوت يعمل
"""
    await message.answer(text)


# ==================================
# /users
# ==================================
@router.message(Command("users"))
async def users_cmd(message: Message):
    if not is_admin(message.from_user.id):
        return

    await message.answer("👥 نظام المستخدمين سيضاف لاحقًا")


# ==================================
# /clean
# ==================================
@router.message(Command("clean"))
async def clean_cmd(message: Message):
    if not is_admin(message.from_user.id):
        return

    removed = 0

    for folder in [DOWNLOAD_DIR, OUTPUT_DIR]:
        for file in os.listdir(folder):
            path = os.path.join(folder, file)

            try:
                os.remove(path)
                removed += 1
            except:
                pass

    await message.answer(f"🧹 تم حذف {removed} ملف مؤقت")


# ==================================
# /broadcast
# ==================================
@router.message(Command("broadcast"))
async def broadcast_cmd(message: Message):
    if not is_admin(message.from_user.id):
        return

    await message.answer("📢 نظام البرودكاست سيضاف لاحقًا")
