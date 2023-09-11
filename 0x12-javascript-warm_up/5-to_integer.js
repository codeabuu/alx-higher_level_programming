#!/usr/bin/node

// Get the first argument from the command line
const arg = process.argv[2];

//convert the argument to an integer
const intValue = parseInt(arg);

// Check if the result is not NaN (isNaN returns true for NaN)
if (!isNaN(intValue)) {
  // Print the integer value
  console.log(`My number: ${intValue}`);
} else {
  // Print "Not a number" if the conversion failed
  console.log('Not a number');
}
