#! /usr/bin/env node
"use strict";

/**
 * Fibonacci iterative algorithm.
 * @param {number} n - Size of the sequence to be generated.
 * @return {number} - Value of n-th Fibonacci number.
 */
function F(n) {
  if (n < 0) {
    return 'Error no negative numbers allowed!';
  }
  n = Math.round(n);
  if (n == 0 || n == 1) {
    return n;
  }
  let F2 = 0;
  let F1 = 1;
  let F0;
  while (n > 1) {
    F0 = F1 + F2;
    F2 = F1;
    F1 = F0;
    n--;
  }
  return F0;
}

console.log(F(10))
