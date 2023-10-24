FROM python:3.9

WORKDIR /app

# Копіюємо файли з кореневої папки вашого проекту в контейнер
COPY . /app

# Встановлюємо залежності Django
RUN pip install -r /app/requirements

EXPOSE 8000

# Запускаємо сервер Django
CMD ["python", "/app/library/manage.py", "runserver", "0.0.0.0:8000"]


