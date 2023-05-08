From python:3.6.9

WORKDIR /app

COPY . .

CMD ["python", "main.py"]