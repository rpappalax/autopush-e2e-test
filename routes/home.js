'use strict';

module.exports = {
  method: 'GET',
  path:'/',
  config: {
    handler: function (req, reply) {
      console.log('/ - ua:' + JSON.stringify(req.headers));
      //reply('This is the autopush-e2e-test app server. Go to: <a href="http://localhost:8000">TEST PAGE</a>');
      reply('This is the autopush-e2e-test app server. Go to: <a href="http://localhost:8201">TEST PAGE</a>');
    }
  }
};
