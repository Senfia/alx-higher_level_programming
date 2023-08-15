#!/usr/bin/node

let cou = 0;

exports.logMe = function count (item) {
  console.log(`${counter}: ${item}`);
  cou += 1;
};
