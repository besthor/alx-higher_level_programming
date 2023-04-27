#!/usr/bin/node
# a script that reads and prints the content of a file.

const fs = require('fs').promises;

fs.readFile(process.argv[2], 'utf-8')
  .then(content => console.log(content))
  .catch(error => console.log(error));
