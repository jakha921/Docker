FROM python:3.9

# go this directory to copy files
#WORKDIR /code

# all files to container
COPY . .

# install necessary packages for container
RUN pip install -r requirements.txt

# copy app.py file to container
COPY ./code /code/

# commands to run
CMD ["python", "./code/main.py"]
