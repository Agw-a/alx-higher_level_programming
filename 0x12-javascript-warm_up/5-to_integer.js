#!/usr/bin/node
if (isNaN(Number(process.argv[2]))) {
  console.log('Not a number');
} else {
  console.log('My Number: ' + Number(process.argv[2]));
}
