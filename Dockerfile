FROM python:3.9

RUN mkdir /app

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . . 

CMD ["gunicorn", "app.main:app", "--workers", "3", "uvicorn.workers.UvicornWorker", "--bind=0.0.0.0:8000"]
