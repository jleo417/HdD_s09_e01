FROM python:3.11-slim
WORKDIR /app
RUN pip install --no-cache-dir numpy pandas openpyxl
COPY s09_e01.py .