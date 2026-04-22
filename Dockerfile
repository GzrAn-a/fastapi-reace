FROM python:3.13.2

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY ./src /code/src
COPY ./main.py /code/main.py


CMD ["fastapi","run","/code/main.py","--proxy-headers","--port","8000"]

