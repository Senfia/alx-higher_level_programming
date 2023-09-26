#!/usr/bin/node

// Import the 'request' module
const request = require('request');

const { argv } = require('process');

// Make a request to the specified URL
const BaseUrl = 'https://swapi-api.hbtn.io/api';
request(BaseUrl + '/films/' + argv[2], (error, response, body) => {
  if (error) {
    console.error(error);
  }
  console.log(JSON.parse(body).title);
});
