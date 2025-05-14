# Вибираємо Python-образ
FROM python:3.12-slim

# Встановлюємо робочу директорію в контейнері
WORKDIR /app

# Копіюємо всі файли у контейнер
COPY . .

# Встановлюємо залежності
RUN pip install --no-cache-dir -r requirements.txt

# Запускаємо скрипт
CMD ["python", "main.py"]
