FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt ./
RUN python -m venv /app/venv \
    && /app/venv/bin/pip install --no-cache-dir --upgrade pip \
    && /app/venv/bin/pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["sh", "-c", "sleep 20 && ./venv/bin/python seed.py && ./venv/bin/gunicorn -b 0.0.0.0:8000 run:app"] 