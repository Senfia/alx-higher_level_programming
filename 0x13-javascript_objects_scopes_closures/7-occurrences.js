#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  let numb = 0;
  for (let i = 0; i < list.length; i++) {
    if (list[i] === searchElement) {
      numb++;
    }
  }
  return numb;
};
