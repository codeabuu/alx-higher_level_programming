#!/usr/bin/node

// Check if there are any arguments passed (excluding the script name)
if (process.argv.length <= 2) {
  console.log('No argument');
} else {
  // Print the first argument (index 2 in the argv array)
  console.log(process.argv[2]);
}
