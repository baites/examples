#! /usr/bin/env node

/**
 * Fibonacci closed-form expression.
 * @param {number} n - Size of the sequence to be generated.
 * @return {number} - Value of n-th Fibonacci number.
 */
function F(n) {
  if (n < 0) {
    return 'Error no negative numbers allowed!';
  }
  n = Math.round(n);
  return Math.round(Math.exp(n*Math.log(1.6180339897) - 0.80471895621705));
}

console.log(F(Number(process.argv[2])))
