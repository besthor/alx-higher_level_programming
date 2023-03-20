#!/usr/bin/node
// using destruct
// using slice(2) to start the slice from the third element of the process.argv array,
// skipping over the node command and the name of the script itself

const [arg] = process.argv.slice(2);

// using an if...else statement to check if arg exists
if (!arg) {
  console.log('No argument');

//  Otherwise, we print arg using console.log(...)
} else {
  console.log(arg);
}
