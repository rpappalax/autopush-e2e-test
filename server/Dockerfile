FROM mhart/alpine-node:8
	
COPY . /app

WORKDIR /app

RUN  apk add --update \
     nodejs \
     nodejs-npm \
     git \

     && rm /var/cache/apk/*
RUN npm install

CMD ["node", "/app/index.js"]
