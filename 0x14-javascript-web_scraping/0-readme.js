#!/usr/bin/node
# a script that reads and prints the content of a file.

const fs = require('fs');
const filename = process.argv[2];

fs.readFile(filename, 'utf-8', (error, content) => {
  if (error) {
    console.log(error);
  } else {
    console.log(content);
  }
});
