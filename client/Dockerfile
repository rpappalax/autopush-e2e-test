FROM selenium/standalone-firefox-debug

USER root

WORKDIR /app

COPY . /app
COPY ./conftest.py /app

#RUN apt-get update && \
#    apt-get install -y python python-dev python-pip python-virtualenv && \
#    rm -rf /var/lib/apt/lists/* && \
#    pip install -r requirements/tests.txt

#CMD pytest --driver Firefox --base-url http://localhost:8201 
