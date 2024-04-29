FROM python:3.12-alpine

WORKDIR /app

COPY . . 

RUN apk add g++ jpeg-dev zlib-dev libjpeg make
RUN pip3 install matplotlib
RUN pip install -r requirements.txt

CMD [ "echo", "'All finished!!'" ]