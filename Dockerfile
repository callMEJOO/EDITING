FROM python:3.11-bullseye

WORKDIR /app

# تثبيت ffmpeg
RUN apt-get update && \
    apt-get install -y ffmpeg && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# نسخ ملفات المشروع
COPY . .

# تثبيت المكتبات
RUN pip install --no-cache-dir -r requirements.txt

# تشغيل البوت
CMD ["python", "main.py"]
