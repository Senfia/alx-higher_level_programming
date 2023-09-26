#!/usr/bin/node

// Import the 'request' module
const request = require('request');

// Define the URL to make a request to (provided as a command-line argument)
const url = process.argv[2];

// Make a request to the specified URL
request(url, function(error, response) {
  if (error === null) {
    // If there is no error, print the HTTP status code
    console.log('HTTP Status Code:', response.statusCode);
  }
});

