#!/usr/bin/node

const args = process.argv;

if (args.length > 2 && Number.isInteger(parseInt(args[2])) === true) {
  for (let i = 0; i < args[2]; i++) {
    let row = '';
    for (let j = 0; j < args[2]; j++) {
      row += 'X';
    }
    console.log(row);
  }
} else {
  console.log('Missing size');
}
