#!/usr/bin/node
const request = require('request');

// Get the URL from the command line argument
const url = process.argv[2];

// Make a GET request to the URL
request.get(url, (error, response) => {
  if (error) {
    console.error('error:', error.message);
  } else {
    console.log('code:', response.statusCode);
  }
});
