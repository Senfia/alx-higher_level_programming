#!/usr/bin/node
const fs = require('fs');

// reads and prints the content of a file
fs.readFile(process.argv[2], 'utf8', function (err, contents) {
  if (contents === undefined) {
    console.log(err);
  } else {
    console.log(contents);
  }
});
