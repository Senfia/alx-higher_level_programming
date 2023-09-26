#!/usr/bin/node

// computes the number of tasks completed by user id

const request = require('request');
const baseUrl = process.argv[2];

request(baseUrl, function (error, response, body) {
  if (error) {
    console.log(error);
  }
  const data = JSON.parse(body);
  const dict = {};
  for (let item = 0; item < data.length; item++) {
    const id = data[item].userId;
    if (data[item].completed === true) {
      if (dict[id] === undefined) {
        dict[id] = 1;
      } else {
        dict[id] += 1;
      }
    }
  }
  console.log(dict);
});
