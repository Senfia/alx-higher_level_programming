#!/usr/bin/node

// Import necessary modules
const request = require('request');
const { argv } = require('process');

// Function to fetch and print character names in order
function order (characters, idx) {
  if (idx >= characters.length) {
    return;
  }
  request(characters[idx], function (err, response, body) {
    if (err) {
      console.log(err);
    } else if (response.statusCode === 200) {
      const person = JSON.parse(body);
      console.log(person.name);
      // Recursively call the 'order' function for the next character
      order(characters, ++idx);
    } else {
      console.log('Error occurred. Status code: ' + response.statusCode);
    }
  });
}

// Define the base URL for the Star Wars API
const url = 'https://swapi-api.hbtn.io/api/films/';
const episode = argv[2];

// Make a request to fetch movie details
request(url + episode, function (err, response, body) {
  if (err) {
    console.log(err);
  } else if (response.statusCode === 200) {
    const movieData = JSON.parse(body);
    // Start fetching and printing character names in order
    order(movieData.characters, 0);
  } else {
    console.log('Error occurred. Status code: ' + response.statusCode);
  }
});
