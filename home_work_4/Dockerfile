# Используем базовый образ
FROM ubuntu:20.04

# Устанавливаем Python и pip
RUN apt-get update && \
    apt-get install -y python3 python3-pip

# Устанавливаем рабочую директорию
WORKDIR /app

# Копируем файлы в контейнер
COPY . /app

# Устанавливаем переменную окружения PYTHONUNBUFFERED
ENV PYTHONUNBUFFERED=1

# Устанавливаем зависимости
RUN pip3 install -r /app/requirements.txt


# Указываем команду для запуска приложения
CMD ["python3", "app.py"]

