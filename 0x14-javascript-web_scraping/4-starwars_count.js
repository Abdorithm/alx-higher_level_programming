#!/usr/bin/node

const request = require('request');

// Get the URL from the command line arguments
const apiUrl = process.argv[2];

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

  // Iterate through the "results" array and count occurrences of the specified URL in the "characters" array
  data.results.forEach(result => {
    result.characters.forEach(character => {
      if (character === 'https://swapi-api.alx-tools.com/api/people/18/') {
        counter++;
      }
    });
  });

  // Print the counter
  console.log(counter);
});
