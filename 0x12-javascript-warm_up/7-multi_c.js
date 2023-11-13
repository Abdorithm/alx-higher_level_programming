#!/usr/bin/node

const args = process.argv;

if (args.length > 2) {
  for (let i = 0; i < args[2]; i++) {
    console.log('C is cool');
  }
} else {
  console.log('Missing number of occurrences');
}
