#!/usr/bin/node
# a script that reads and prints the content of a file.

const fs = require('fs');

function readFile(filePath) {
  fs.readFile(filePath, 'utf-8', (err, data) => {
    if (err) {
      console.error(err);
      return;
    }

    console.log(data);
  });
}


