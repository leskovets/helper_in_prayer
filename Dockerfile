FROM python:3.12.1

COPY . /app/

WORKDIR /app

RUN python -m pip install -r requirements.txt

ENTRYPOINT ["python", "main.py"]