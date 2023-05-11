#!/usr/bin/node

const { dict } = require('./101-data');

const usersByOccurrence = {};

for (const [userId, occurrence] of Object.entries(dict)) {
  if (usersByOccurrence[occurrence]) {
    usersByOccurrence[occurrence].push(userId);
  } else {
    usersByOccurrence[occurrence] = [userId];
  }
}

console.log(usersByOccurrence);
