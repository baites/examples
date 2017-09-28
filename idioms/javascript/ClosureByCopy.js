#! /usr/bin/env node
"use strict";

/**
 * Create closure forcing capture by copy or value
 * @param value - Value of context
 */
function CreateClosure(value) {
  const context = JSON.parse(
    JSON.stringify(value)
  );
  function Method() {
    return JSON.parse(
      JSON.stringify(context)
    );
  }
  return Method;
}

// Creating closure with a unmutable object (a string)
// This behaves as if context is captured by copy or value
const unmutable = 'A'
const closureA = CreateClosure(unmutable);
console.log('context in closureA: ', closureA());

// Creating closure with a mutable object (a list)
// This behaves as if context is captured by reference
let mutable = ['B'];
const closureB = CreateClosure(mutable);
console.log('context in closureB: ', closureB());

// It is possible to change of the value of the context
mutable[0] = 'C';
console.log('context in closureB: ', closureB());

// It is not event possible to get a refence to context
mutable = closureB();
mutable[0] = 'C';
console.log('context in closureB: ', closureB());
