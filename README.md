# Docker 

[pdf](https://cloclo56.datacloudmail.ru/public/view/7Yib95YUzqRtDr4AcoRpmbyCzbLr5DKZ2RfUje6Dmdqq7Wd4rDBgFwDDogC2JcVBeQ86zv/no/%D0%9E%D1%81%D0%BD%D0%BE%D0%B2%D1%8B_Docker__Docker_%D0%B8_Python.pdf)


```Dockerfile
Dockerfile

FROM python:3.9.4

ADD main.py .

COPY requirements.txt .
RUN pip3 install -r requirements.txt

CMD ["python", "./main.py"]
```

```shell
cmd

docker build -t <img_name> .  # build the image and show directory

docker run <img_name> # run docker img       
```


