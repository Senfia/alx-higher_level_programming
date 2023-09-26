#!/usr/bin/node

// Import necessary modules
const request = require('request');
const { argv } = require('process');

// Define the base URL for the Star Wars API
const BaseUrl = 'https://swapi-api.hbtn.io/api/films/';

// Function to make a request and return a promise
function MakeRequest (url) {
  return new Promise(function (resolve, reject) {
    request(url, (error, response, body) => {
      if (!error && response.statusCode === 200) {
        resolve(body);
      } else {
        reject(error);
      }
    });
  });
}

// Async function to fetch movie details and characters
async function main () {
  try {
    // Fetch movie details
    const movie = await MakeRequest(BaseUrl + argv[2]);
    const movieData = JSON.parse(movie);

    // Extract characters array from movie data
    const characters = movieData.characters;

    // Fetch and print character names
    for (const characterUrl of characters) {
      const character = await MakeRequest(characterUrl);
      const characterData = JSON.parse(character);
      console.log(characterData.name);
    }
  } catch (error) {
    console.error('Error:', error);
  }
}

// Invoke the main function
main();
