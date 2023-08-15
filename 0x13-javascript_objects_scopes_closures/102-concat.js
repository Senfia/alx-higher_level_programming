#!/usr/bin/node

const fs = require('fs');
let data = '';

data = data.concat(fs.readFileSync(process.argv[2]));
data = data.concat(fs.readFileSync(process.argv[3]));
fs.writeFileSync(process.argv[4], data);
