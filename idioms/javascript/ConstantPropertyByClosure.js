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

class A {
  // Class constructor
  constructor(value) {
    ConstantProperty(this, 'constant', value);
  }
  // A non property setter for constant.
  setConstant(value) {
    this.constant = value;
  }
}

const mutable = {
    'A': [1, 2],
    'B': 'cannot be change'
};

// Initialize object with a mutable object
const a = new A(mutable);
// Print object
console.log(a.constant);

// Try to change constant property
// by updating object referred by mutable
mutable['B'] = 'can be changed';
console.log(a.constant);

// Try to change constant property
// by updating object return by a.constant
a.constant['B'] = 'can be changed';
console.log(a.constant);

// Try to modify constant property
try {
    a.constant = { 'A': 'new' };
    console.log(a.constant);
} catch(error) {
    console.log(error);
}

// Try to modify constant property
try {
    a.setConstant({ 'A': 'new' });
    console.log(a.constant);
} catch(error) {
    console.log(error)
}
