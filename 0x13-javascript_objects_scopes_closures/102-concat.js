#!/usr/bin/node
const fs = require('fs');

if (process.argv.length < 5) {
  console.log('Usage: node concat.js <file1> <file2> <destination>');
  process.exit(1);
}

const file1Path = process.argv[2];
const file2Path = process.argv[3];
const destPath = process.argv[4];

fs.readFile(file1Path, (err, data1) => {
  if (err) throw err;
  fs.readFile(file2Path, (err, data2) => {
    if (err) throw err;
    fs.writeFile(destPath, Buffer.concat([data1, data2]), (err) => {
      if (err) throw err;
      console.log(`Successfully concatenated ${file1Path} and ${file2Path} into ${destPath}`);
    });
  });
});
