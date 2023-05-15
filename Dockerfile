FROM python:3
# python이 실행되기 전에 compile을 거치면서 .pyc 파일을 생성하는데, docker에서는 불필요해 그것을 방지해줌
ENV PYTHONDONTWRITEBYTECODE=1
# 버퍼링을 제거해주기 위해 사용
ENV PYTHONUNBUFFERED=1

#RUN apk update
#
#RUN apk add build-base python3-dev py-pip jpeg-dev zlib-dev
#COPY requirements.txt /code/

WORKDIR /code
COPY requirements.txt /code/
RUN pip install -r requirements.txt

COPY . /code/