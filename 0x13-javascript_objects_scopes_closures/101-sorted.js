#!/usr/bin/node

const dict = require('./101-data').dict;
const nwDict = {};

Object.keys(dict).map(function (key) {
  if (!Array.isArray(nwDict[dict[key]])) {
    nwDict[dict[key]] = [];
  }
  nwDict[dict[key]].push(key);
});

console.log(nwDict);
