'use strict';

var Hapi = require('hapi');
var Path = require('path');
var Inert = require('inert');

startServer(8201);

function startServer(port) {
  var server = new Hapi.Server();
  server.connection({
    host: process.env.HAPI_SERVER || '0.0.0.0',
    port: process.env.PORT || port,
    routes: { cors: true }
  });

  server.register(Inert, () => {});

  // route to test page - http://localhost:8201
  server.route({
    path: "/{p*}",
    method: "GET",
    handler: {
        directory: {
            path: './client',
            redirectToSlash: true,
            index: true,
        }
    }
  });

  // route to app server (used by test page to talk to autopush) 
  server.route([
    require("./routes/notify")
  ]);

  server.start(function () {
    console.log('Server running at: %s', server.info.uri);
  });

}
