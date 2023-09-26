#!/usr/bin/node
// Import the 'request' module
const request = require('request');

// Make a request to the specified URL
request(process.argv[2], function (error, response) {
  if (error == null) {
    console.log('code: ' + response.statusCode);
  }
});
