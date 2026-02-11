FROM python:3.13.9-slim

WORKDIR /app
COPY . .

CMD ["python", "app.py"]
