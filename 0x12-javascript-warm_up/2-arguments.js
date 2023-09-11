#!/usr/bin/env node

// Check the number of command-line arguments
const numArgs = process.argv.length - 2; // Subtracting 2 to exclude 'node' and the script file name

if (numArgs === 0) {
  console.log('No argument');
} else if (numArgs === 1) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
