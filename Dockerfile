FROM python:3.11-slim

WORKDIR /app

COPY . /app

RUN apt update && apt install -y ffmpeg
RUN pip install --no-cache-dir -r bot/requirements.txt

CMD ["python", "bot/main.py"]
