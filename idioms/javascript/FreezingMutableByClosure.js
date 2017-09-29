#! /usr/bin/env node
"use strict";

// Create a closure protected constant copy of value.
function ConstantProperty(object, name, value){
  const cache = JSON.parse(
    JSON.stringify(value)
  );
  Object.defineProperty(object, name, {
    get: () => JSON.parse(
      JSON.stringify(cache)
    )
  });
}

// Literally in js FreezingMutable == ConstantProperty
const FreezingMutable = ConstantProperty;

const mutable = {
    'A': [1, 2],
    'B': 'cannot be change'
};

// Freezing mutable by setting a ContantProperty in global
FreezingMutable(global, 'constant', mutable);
console.log(constant);

// Print object
console.log(constant);

// Try to change constant property
// by updating object referred by "mutable"
mutable['B'] = 'can be changed';
console.log(constant);

// Try to change constant property
// by updating object return by constant
constant['B'] = 'can be changed';
console.log(constant);
