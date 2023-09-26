#!/usr/bin/node

// gets the contents of a webpage and stores it in a file
// The first argument is the URL to request
// The second argument is the file path to store the body response
// The file is UTF-8 encoded
const request = require('request');
const fs = require('fs');
const baseUrl = process.argv[2];
const file = process.argv[3];
let data = '';

request(baseUrl, function (error, response, body) {
  if (error) {
    console.log(error);
  }
  data = body;
  fs.writeFile(file, data, 'utf-8', function write (err, data) {
    if (err) {
      return console.log(err);
    }
  });
});
