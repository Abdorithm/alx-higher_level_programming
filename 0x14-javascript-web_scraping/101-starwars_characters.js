#!/usr/bin/node

// Import the request module
const request = require('request');

// Get the movie ID from the command line arguments
const movieID = process.argv[2];

// Construct the URL for the Star Wars movie API
const url = 'https://swapi-api.hbtn.io/api/films/' + movieID;

// Send a GET request to the Star Wars movie API
request(url, async (error, response, body) => {
  // Handle errors
  if (error) {
    console.error(error);
    return;
  }

  // Parse the JSON response body
  const result = JSON.parse(body);

  // Iterate through each character URL in the movie
  for (const charURL of result.characters) {
    // Make a request to fetch character details
    await new Promise((resolve, reject) => {
      request(charURL, (err, r, body) => {
        if (err) {
          reject(err);
        } else {
          // Parse the character details and print the character name
          console.log(JSON.parse(body).name);
          resolve();
        }
      });
    });
  }
});
