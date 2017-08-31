#! /usr/bin/env node
const request = require('request-promise-native');
const util = require('util');

request({
  uri: 'http://bsemetrics:8888/bm/pool-hosts%20--format%3Djson%20-w%20hostname%3Dbat4004glnx86',
  json: true
}).then((data) => {
  console.log(util.inspect(data, {depth: null, colors: true}));
}).catch((error) => {
  console.log(error);
});
