# callbacks.py

import os
import asyncio

from aiogram import Router, F
from aiogram.types import CallbackQuery, FSInputFile

from config import (
    OUTPUT_DIR,
    BUSY_TEXT,
    DONE_TEXT,
    ERROR_TEXT,
    FFMPEG_PRESET
)

from main_menu import main_menu
from quality_menu import quality_menu
from video import user_videos

router = Router()


# ==================================
# الرئيسية
# ==================================
@router.callback_query(F.data == "home")
async def home_callback(call: CallbackQuery):
    await call.message.edit_text(
        "🎬 القائمة الرئيسية",
        reply_markup=main_menu()
    )
    await call.answer()


# ==================================
# ضغط فيديو
# ==================================
@router.callback_query(F.data == "compress")
async def compress_callback(call: CallbackQuery):
    await call.message.edit_text(
        "📦 اختر جودة الضغط:",
        reply_markup=quality_menu()
    )
    await call.answer()


# ==================================
# أزرار عامة
# ==================================
@router.callback_query(F.data == "status")
async def status_callback(call: CallbackQuery):
    await call.answer("🟢 السيرفر يعمل", show_alert=True)


@router.callback_query(F.data == "vip")
async def vip_callback(call: CallbackQuery):
    await call.answer("👑 قريبًا", show_alert=True)


@router.callback_query(F.data == "settings")
async def settings_callback(call: CallbackQuery):
    await call.answer("🎚 قريبًا", show_alert=True)


@router.callback_query(F.data == "convert")
async def convert_callback(call: CallbackQuery):
    await call.answer("🎞 قريبًا", show_alert=True)


@router.callback_query(F.data == "fast")
async def fast_callback(call: CallbackQuery):
    await call.answer("⚡ قريبًا", show_alert=True)


# ==================================
# ضغط الفيديو
# ==================================
@router.callback_query(F.data.startswith("q_"))
async def quality_callback(call: CallbackQuery):
    user_id = call.from_user.id

    if user_id not in user_videos:
        await call.answer("❌ ارفع فيديو أولاً", show_alert=True)
        return

    crf = call.data.split("_")[1]

    input_path = user_videos[user_id]
    output_path = os.path.join(
        OUTPUT_DIR,
        f"{user_id}_compressed.mp4"
    )

    await call.message.answer(BUSY_TEXT)

    cmd = [
        "ffmpeg",
        "-y",
        "-i", input_path,
        "-vcodec", "libx264",
        "-preset", FFMPEG_PRESET,
        "-crf", crf,
        "-movflags", "+faststart",
        output_path
    ]

    process = await asyncio.create_subprocess_exec(
        *cmd,
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE
    )

    await process.communicate()

    if os.path.exists(output_path):
        video_file = FSInputFile(output_path)

        await call.message.answer_video(
            video=video_file,
            caption=DONE_TEXT
        )
    else:
        await call.message.answer(ERROR_TEXT)

    await call.answer()
