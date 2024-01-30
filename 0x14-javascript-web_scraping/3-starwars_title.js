#!/usr/bin/node

const request = require('request');

// Get the URL from the command line arguments
const apiUrl = "https://swapi-api.alx-tools.com/api/films/" + process.argv[2];

// Counter to count occurrences of the specified URL
let counter = 0;

// Send a GET request to the specified URL
request.get(apiUrl, (error, response, body) => {
  if (error || response.statusCode !== 200) {
    console.error('Error:', error || `Status code: ${response.statusCode}`);
    return;
  }

  // Parse the JSON response body
  const data = JSON.parse(body);

  // Print title of episode
  console.log(data.title);
});
