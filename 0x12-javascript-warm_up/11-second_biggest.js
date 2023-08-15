#!/usr/bin/node

if (process.argv.length < 4) {
  console.log('0');
} else {
  const sizes = process.argv.length;
  const intss = [];
  for (let i = 2; i < sizes; i++) {
    intss[i - 2] = parseInt(process.argv[i]);
  }
  intss.sort(function (a, b) { return b - a; });
  console.log(intss[1]);
}
