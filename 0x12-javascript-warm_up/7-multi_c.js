#!/usr/bin/node

let myVar = parseInt(process.argv[2]);
if (isNaN(myVar) || process.argv[2] === undefined) {
  console.log('Missing number of occurences');
} else {
  while (myVar > 0) {
    console.log('C is fun');
    myVar--;
  }
}
