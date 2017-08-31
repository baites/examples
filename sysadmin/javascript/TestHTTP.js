#! /usr/bin/env node
const http = require('http');
const util = require('util');

function pprint(doc){
  object = JSON.parse(doc);
  console.log(util.inspect(object, {depth: null, colors: true}))
}

http.get({
    host: 'bsemetrics',
    port: 8888,
    path: '/bm/pool-hosts%20--format%3Djson%20-w%20hostname%3Dbat4004glnx86',
    json: true
  }, (response) => {
    //response.setEncoding('utf8');
    response.on('data', (data) => pprint(data));
  }
).on('error', (error) => console.log(error));
