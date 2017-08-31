#! /usr/bin/env node
"use strict";

function F(n) {
  if (n < 0) {
    return 'Error no negative numbers allowed!';
  }
  n = Math.round(n);
  if (n == 0 || n == 1) {
    return n;
  }
  return F(n-1) + F(n-2);
}

console.log(F(10))
