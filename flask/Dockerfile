# Dockerfile
FROM python:3.8.2-slim-buster

RUN apt update && apt install -y libaio1 wget
RUN apt install -y unzip
RUN apt install -y gcc python3-dev
RUN pip install --upgrade pip

WORKDIR /opt/oracle
RUN wget https://download.oracle.com/otn_software/linux/instantclient/19800/instantclient-basic-linux.x64-19.8.0.0.0dbru.zip && \
    unzip instantclient-basic-linux.x64-19.8.0.0.0dbru.zip && \
    rm -f instantclient-basic-linux.x64-19.8.0.0.0dbru.zip 
RUN cd /opt/oracle/instantclient_19_8 && rm -f *jdbc* *occi* *mysql* *README *jar uidrvci genezi adrci
RUN echo /opt/oracle/instantclient_19_8 > /etc/ld.so.conf.d/oracle-instantclinet.conf && \
    ldconfig
RUN  pip3 install cx_Oracle

WORKDIR /app
ADD . /app

RUN        pip install -r requirements.txt
EXPOSE     8000
# For this statement to work you need to add the next two lines into Pipfilefile
# [scripts]
# server = "python manage.py runserver 0.0.0.0:8000"
#ENTRYPOINT ["pipenv", "run", "server"]
CMD ["uwsgi", "app.ini"]
