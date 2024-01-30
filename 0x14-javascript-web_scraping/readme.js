#!/usr/bin/env node

// Import the file system module
const fs = require('fs');

// Path to the file you want to read
const filePath = process.argv[2];

// Read the contents of the file
fs.readFile(filePath, 'utf8', (err, data) => {
  if (err) {
    console.error('Error reading file:', err);
    return;
  }

  // Print the contents of the file
  console.log(data);
});
