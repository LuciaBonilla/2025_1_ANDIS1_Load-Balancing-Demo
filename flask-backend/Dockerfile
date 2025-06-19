FROM python:3.11-slim

# Directorio de trabajo dentro del contenedor.
WORKDIR /app

COPY app.py .

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

ENV BACKEND_ID=default
CMD ["python", "app.py"]