# compressor.py

import os
import asyncio

from config import OUTPUT_DIR, FFMPEG_PRESET


# ==================================
# إنشاء اسم ملف الإخراج
# ==================================
def output_file(user_id: int) -> str:
    return os.path.join(
        OUTPUT_DIR,
        f"{user_id}_compressed.mp4"
    )


# ==================================
# ضغط الفيديو
# input_path = مسار الفيديو الأصلي
# crf = الجودة (24 / 28 / 32)
# ==================================
async def compress_video(
    user_id: int,
    input_path: str,
    crf: int = 28
) -> tuple:

    output_path = output_file(user_id)

    cmd = [
        "ffmpeg",
        "-y",
        "-i", input_path,

        # فيديو
        "-c:v", "libx264",
        "-preset", FFMPEG_PRESET,
        "-crf", str(crf),

        # صوت
        "-c:a", "aac",
        "-b:a", "128k",

        # تشغيل سريع
        "-movflags", "+faststart",

        output_path
    ]

    process = await asyncio.create_subprocess_exec(
        *cmd,
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE
    )

    stdout, stderr = await process.communicate()

    if process.returncode == 0 and os.path.exists(output_path):
        return True, output_path

    return False, stderr.decode(errors="ignore")


# ==================================
# حذف ملف واحد
# ==================================
def remove_file(path: str):
    try:
        if os.path.exists(path):
            os.remove(path)
    except:
        pass


# ==================================
# حذف ملفات المستخدم
# ==================================
def clean_user_files(user_id: int):
    try:
        for file in os.listdir(OUTPUT_DIR):
            if str(user_id) in file:
                os.remove(os.path.join(OUTPUT_DIR, file))
    except:
        pass
