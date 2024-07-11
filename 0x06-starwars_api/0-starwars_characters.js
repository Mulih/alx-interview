#!/usr/bin/node

const request = require('request');

const req = (arr, j) => {
  if (j === arr.length) return;
  request(arr[j], (err, response, body) => {
    if (err) {
      throw err;
    } else {
      console.log(JSON.parse(body).name);
      req(arr, j + 1);
    }
  });
};

request(
  `https://swapi-api.hbtn.io/api/films/${process.argv[2]}`,
  (err, response, body) => {
    if (err) {
      throw err;
    } else {
      const chars = JSON.parse(body).characters;
      req(chars, 0);
    }
  }
);
