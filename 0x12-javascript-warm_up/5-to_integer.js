#!/usr/bin/node

const arg = parseInt(process.argv[2]);

if (Number.isInteger(arg) === true) {
  console.log(arg);
} else {
  console.log('Not a number');
}
