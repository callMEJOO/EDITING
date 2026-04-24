# utils/helpers.py

import os
import math
import time
from datetime import datetime

# ==================================
# تحويل الحجم لصيغة مقروءة
# ==================================
def format_size(size_bytes: int) -> str:
    if size_bytes == 0:
        return "0 B"

    units = ["B", "KB", "MB", "GB", "TB"]
    index = int(math.floor(math.log(size_bytes, 1024)))
    power = math.pow(1024, index)
    size = round(size_bytes / power, 2)

    return f"{size} {units[index]}"

# ==================================
# حجم ملف
# ==================================
def get_file_size(path: str) -> str:
    if not os.path.exists(path):
        return "0 B"

    return format_size(os.path.getsize(path))

# ==================================
# نسبة التوفير
# ==================================
def compression_percent(before_path: str, after_path: str) -> int:
    if not os.path.exists(before_path):
        return 0

    if not os.path.exists(after_path):
        return 0

    before = os.path.getsize(before_path)
    after = os.path.getsize(after_path)

    if before == 0:
        return 0

    saved = before - after
    percent = (saved / before) * 100

    return round(percent)

# ==================================
# وقت حالي
# ==================================
def now_time() -> str:
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# ==================================
# مدة التنفيذ
# ==================================
def elapsed(start_time: float) -> str:
    sec = int(time.time() - start_time)

    mins = sec // 60
    secs = sec % 60

    if mins > 0:
        return f"{mins}m {secs}s"

    return f"{secs}s"

# ==================================
# إنشاء فولدر
# ==================================
def ensure_folder(path: str):
    os.makedirs(path, exist_ok=True)

# ==================================
# تنظيف اسم ملف
# ==================================
def safe_filename(name: str) -> str:
    banned = ['\\', '/', ':', '*', '?', '"', '<', '>', '|']
    for char in banned:
        name = name.replace(char, "_")
    return name.strip()

# ==================================
# رسالة إحصائيات الضغط
# ==================================
def compression_report(before_path: str, after_path: str) -> str:
    before = get_file_size(before_path)
    after = get_file_size(after_path)
    percent = compression_percent(before_path, after_path)

    return f"""
📊 تقرير الضغط

📥 قبل: {before}
📤 بعد: {after}
💾 التوفير: {percent}%
"""
