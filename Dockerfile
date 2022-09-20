# Dockerfile, Image, Container
FROM python:3.9.4

ADD main.py .

COPY requirements.txt .
RUN pip3 install -r requirements.txt

CMD ["python", "./main.py"]