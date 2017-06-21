# autopush-e2e-test 

## Description

Mozilla web push test page for autopush server

Includes a backend app server that wraps web-push lib and sends encrypted payload via HTTP POST to Mozilla's web push service: 
https://github.com/mozilla-services/autopush

## Install

```
git clone https://github.com/rpappalax/autopush-e2e-test

cd autopush-e2e-test

npm install
```

## Start App Server 

In terminal window, launch app server

```
node ./index.js
```

App server will run in background (on localhost port 8201)

## Run Test 

Open Firefox browser to:  http://localhost:8201

Execute tests.

Web page will communicate with app server to register, etc. agains Mozilla's web push service.

## Run Test (Docker)

### Summary

The test page and app server can be run from a docker container.
To build your own docker container, follow instructions below.
To use existing container on dockerhub, do the following:

```
docker pull firefoxtesteng/autopush-e2e-test
```

Then follow instructions for Docker Run (below)


### Docker Build

```
docker build -t autopush-e2e-test .
```

### Docker Run

```
docker run -p 8201:8201  autopush-e2e-test
```

Follow instructions for "Run Test" (above)






