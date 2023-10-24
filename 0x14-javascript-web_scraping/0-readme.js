#!/usr/bin/node

const fs = require('fs');
const filename = process.argv[2];

function handleFileRead (error, content) {
  if (error) {
    console.error(error); // Log the error message to the error stream
  } else {
    console.log(content);
  }
}

fs.readFile(filename, 'utf-8', handleFileRead);
