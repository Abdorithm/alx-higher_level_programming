#!/usr/bin/node

const fs = require('fs');
const request = require('request');

// Get URL and file path from command line arguments
const url = process.argv[2];
const filePath = process.argv[3];

// Send a GET request to the specified URL
request.get(url, (error, response, body) => {
  if (error || response.statusCode !== 200) {
    console.error(error || `Status code: ${response.statusCode}`);
    process.exit(1);
  }

  // Write the body response to the specified file
  fs.writeFile(filePath, body, 'utf8', (err) => {
    if (err) {
      console.error(err);
      process.exit(1);
    }
  });
});
