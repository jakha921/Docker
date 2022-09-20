# Create Flask image form Docker

```Dockerfile
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
```

```python
app.py

# add host & if you want can add post as default it is :5000
if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0')
```

```shell
sudo docker build -t <img_name> <directory>     # create own image

sudo docker images  # to see this img

# run on port 8080 on my PC http://localhost:5000/
sudo docker run -d -p 5000(local_post):5000(container_port) <img_name>    
```