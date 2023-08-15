#!/usr/bin/node

let sizes = parseInt(process.argv[2]);
if (isNaN(sizes) || process.argv[2] === undefined) {
  console.log('Missing size');
}
let pstrr = 'X';
for (let i = 0; i < sizes - 1; i++) {
  pstrr += 'X';
}
while (sizes > 0) {
  console.log(pstrr);
  sizes--;
}
