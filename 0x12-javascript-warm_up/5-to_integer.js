#!/usr/bin/node
// using the isNaN() function to check if the first argument (arg) can be converted to an integer.

const arg = process.argv[2];

// using the ! (logical NOT) operator to invert the boolean value returned by isNaN()
// printing the result using template literals to interpolate the value into the output string in the specified format.
if (!isNaN(parseInt(arg))) {
  console.log(`My number: ${parseInt(arg)}`);
// If it can't be converted to an integer, we print "Not a number" instead.
} else {
  console.log('Not a number');
}
