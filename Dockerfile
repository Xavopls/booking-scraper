FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

COPY . /app/

# Expose port dynamically
ARG DJANGO_PORT=8000
ENV DJANGO_PORT=${DJANGO_PORT}

CMD ["sh", "-c", "python manage.py runserver 0.0.0.0:${DJANGO_PORT}"]
