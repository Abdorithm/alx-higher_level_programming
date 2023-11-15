#!/usr/bin/node

const fs = require('fs');

fs.writeFileSync(process.argv[4], fs.readFileSync(process.argv[2]) + fs.readFileSync(process.argv[3]));
