#!/usr/bin/node
// copy the process.argv array
const args = process.argv.slice(2);
let count = 0;
while (args[count]) {
  console.log(args[count]);
  count++;
}
if (count === 0) {
  console.log('No argument');
}
