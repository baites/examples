#! /usr/bin/env node

function F(n) {
  if (n < 0) {
    return 'Error no negative numbers allowed!';
  }
  n = Math.round(n);
  const sqrt5 = Math.sqrt(5);
  const phi = (1+sqrt5)/2;
  return Math.round(phi**n/sqrt5);
}


console.log(F(10));
