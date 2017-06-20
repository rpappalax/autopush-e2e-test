'use strict';

var Hapi = require('hapi');
var Path = require('path');
var Inert = require('inert');

startServer(8201);

function startServer(port) {
  var server = new Hapi.Server();
  server.connection({
    host: process.env.HAPI_SERVER || 'localhost',
    port: process.env.PORT || port,
    routes: { cors: true }
  });

  server.register(Inert, () => {});

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

  server.route([
    require("./routes/notify")
  ]);

  server.start(function () {
    console.log('Server running at: %s', server.info.uri);
  });


}
