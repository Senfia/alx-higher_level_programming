#!/usr/bin/node

// Import the 'request' module
const request = require('request');

const { argv } = require('process');

// Make a request to the specified URL
const Url = 'https://swapi-api.hbtn.io/api';
request(Url + '/films/' + argv[2], (error, response, body) => {
  if (error) {
    console.error(error);
  }
  console.log(JSON.parse(body).title);
});
