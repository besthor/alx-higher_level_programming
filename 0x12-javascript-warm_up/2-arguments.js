#!/usr/bin/node

// calculate the number of arguments passed to the script using 'process.argv.length - 2'
// sbtracting 2 to exclude the 'node' command and the name of the script itself

const argsCount = process.argv.length - 2;

// using 'if...else' statement to check the value of 'argsCount'
// using 'console.log' to print the appropriate message

if (argsCount === 0) {
  console.log('No argument');
} else if (argsCount === 1) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
