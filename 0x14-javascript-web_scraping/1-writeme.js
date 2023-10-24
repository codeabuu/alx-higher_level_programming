#!/usr/bin/node

const fs = require('fs');
const filename = process.argv[2];
const fileContent = process.argv[3];

function handleFileRead (error, content) {
  if (error) {
    console.error(error); // Log the error message to the error stream
  }
}

fs.writeFile(filename, fileContent, 'utf-8', handleFileRead);
