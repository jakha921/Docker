# Dockerfile - this is a comment. Delete me if you want.
FROM python:3.9

# tell who is author
MAINTAINER Jakha 'jakha921@gmail.com'

# copy all files from . to app
COPY . /app

# working directory in container
WORKDIR /app

# run code and install all necessary packages
RUN pip install -r requirement.txt

# run project
CMD ["python", "app.py"]