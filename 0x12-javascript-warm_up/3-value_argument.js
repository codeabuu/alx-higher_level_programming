#!/usr/bin/node

// Check if there are any arguments passed (excluding the script name)
if (process.argv[2] === undefined) {
  console.log('No argument');
} else {
  // Print the first argument (index 2 in the argv array)
  console.log(process.argv[2]);
}
