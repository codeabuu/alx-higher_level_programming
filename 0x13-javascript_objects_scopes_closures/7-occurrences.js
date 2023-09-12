#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  // Initialize a counter for occurrences
  let count = 0;

  // Loop through the array and count occurrences of searchElement
  for (let i = 0; i < list.length; i++) {
    if (list[i] === searchElement) {
      count++;
    }
  }

  // Return the count of occurrences
  return count;
};
