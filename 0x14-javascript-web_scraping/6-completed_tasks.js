#!/usr/bin/node

// Import the request module
const request = require('request');

// Get the API URL from the command line arguments
const apiUrl = process.argv[2];

// Send a GET request to the specified API URL
request(apiUrl, (err, resp, body) => {
  // Handle errors
  if (err) {
    console.error('Error:', err);
    return;
  }

  // Object to store the count of completed tasks for each user
  const completedTasksByUser = {};

  // Parse the JSON response body
  const tasks = JSON.parse(body);

  // Iterate through each task
  for (const task of tasks) {
    // Check if the task is completed
    if (task.completed) {
      // Increment the count of completed tasks for the user
      if (completedTasksByUser[task.userId]) {
        completedTasksByUser[task.userId]++;
      } else {
        completedTasksByUser[task.userId] = 1;
      }
    }
  }

  // Print the count of completed tasks for each user
  console.log(completedTasksByUser);
});
