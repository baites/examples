#! /usr/bin/env node
"use strict";

/**
 * Fibonacci recursive algorithm.
 * @param {number} n - Size of the sequence to be generated.
 * @return {number} - Value of n-th Fibonacci number.
 */
function F(n) {
  if (n < 0) {
    return 'Error no negative numbers allowed!';
  }
  n = Math.round(n);
  if (n < 2) {
    return n;
  }
  return F(n-1) + F(n-2);
}

console.log(F(Number(process.argv[2])))
