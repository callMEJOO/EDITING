# config.py

import os

# ==================================
# BOT SETTINGS
# ==================================
TOKEN = "8206699197:AAGgB7rtI-TvPRkH8HqkZ4Tip3kOUmwOioM"
ADMIN_ID = 8691706370

# ==================================
# PATHS
# ==================================
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

DOWNLOAD_DIR = os.path.join(BASE_DIR, "downloads")
OUTPUT_DIR = os.path.join(BASE_DIR, "outputs")
LOGS_DIR = os.path.join(BASE_DIR, "logs")

# إنشاء المجلدات تلقائيًا
os.makedirs(DOWNLOAD_DIR, exist_ok=True)
os.makedirs(OUTPUT_DIR, exist_ok=True)
os.makedirs(LOGS_DIR, exist_ok=True)

# ==================================
# VIDEO SETTINGS
# ==================================
MAX_VIDEO_SIZE_MB = 2000      # أقصى حجم فيديو (2GB)
DEFAULT_CRF = 28             # الجودة الافتراضية
FFMPEG_PRESET = "fast"

# ==================================
# SECURITY
# ==================================
ADMINS = [8691706370]

# ==================================
# MESSAGES
# ==================================
START_TEXT = """
🎬 Welcome to Video Compress Pro Bot

ارفع الفيديو ثم اختر الخدمة المطلوبة.
"""

BUSY_TEXT = "⏳ جاري معالجة الفيديو..."
DONE_TEXT = "✅ تم الانتهاء بنجاح"
ERROR_TEXT = "❌ حدث خطأ أثناء التنفيذ"
