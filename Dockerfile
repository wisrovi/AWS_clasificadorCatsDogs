FROM tensorflow/tensorflow
MAINTAINER wisrovi.rodriguez@gmail.com
WORKDIR /api

RUN pip3 install flask
RUN pip3 install tensorflow
RUN pip3 install keras
RUN pip3 install Pillow

COPY src .

CMD [ "python3", "./service.py" ]