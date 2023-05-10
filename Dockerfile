From python:3.6.9

WORKDIR /app

COPY . .

RUN python -m unittest test.py

CMD ["python", "main.py"]
