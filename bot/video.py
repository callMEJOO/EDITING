# video.py

import os

from aiogram import Router, F
from aiogram.types import Message

from config import DOWNLOAD_DIR, MAX_VIDEO_SIZE_MB
from quality_menu import quality_menu

router = Router()

# حفظ ملفات المستخدمين مؤقتًا
user_videos = {}


# ==================================
# استقبال الفيديو العادي
# ==================================
@router.message(F.video)
async def receive_video(message: Message):
    user_id = message.from_user.id
    video = message.video

    size_mb = video.file_size / (1024 * 1024)

    if size_mb > MAX_VIDEO_SIZE_MB:
        await message.answer(
            f"❌ حجم الفيديو كبير جدًا.\nالحد الأقصى: {MAX_VIDEO_SIZE_MB} MB"
        )
        return

    await message.answer("📥 جاري تحميل الفيديو...")

    file_info = await message.bot.get_file(video.file_id)

    input_path = os.path.join(DOWNLOAD_DIR, f"{user_id}.mp4")

    await message.bot.download_file(
        file_info.file_path,
        destination=input_path
    )

    user_videos[user_id] = input_path

    await message.answer(
        "✅ تم استلام الفيديو بنجاح.\nاختر الجودة المطلوبة:",
        reply_markup=quality_menu()
    )


# ==================================
# استقبال الفيديو كملف Document
# ==================================
@router.message(F.document)
async def receive_document_video(message: Message):
    doc = message.document

    if not doc.mime_type:
        return

    if "video" not in doc.mime_type:
        return

    user_id = message.from_user.id

    size_mb = doc.file_size / (1024 * 1024)

    if size_mb > MAX_VIDEO_SIZE_MB:
        await message.answer(
            f"❌ حجم الملف كبير جدًا.\nالحد الأقصى: {MAX_VIDEO_SIZE_MB} MB"
        )
        return

    await message.answer("📥 جاري تحميل الملف...")

    file_info = await message.bot.get_file(doc.file_id)

    ext = doc.file_name.split(".")[-1]
    input_path = os.path.join(DOWNLOAD_DIR, f"{user_id}.{ext}")

    await message.bot.download_file(
        file_info.file_path,
        destination=input_path
    )

    user_videos[user_id] = input_path

    await message.answer(
        "✅ تم استلام الملف بنجاح.\nاختر الجودة المطلوبة:",
        reply_markup=quality_menu()
    )
