#!/usr/bin/node

const request = require('request');

const paramiters = {
  url: 'https://swapi-api.alx-tools.com/api/films/:id' + process.argv[2],
  method: 'GET'
};
request(paramiters, function (error, response, body) {
  if (error) {
    console.log(error);
  }
  console.log(JSON.parse(body)['title']);
});
