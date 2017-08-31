#! /usr/bin/env node
"use strict";

function readonly(object, name, value){
  Object.defineProperty(object, name, {
    get: () => value
  });
}

function B() {
  readonly(this, 'constant', 'Susana');
}
const b = new B();
console.log(b.constant);

readonly(global, 'constant', 'victor');
console.log(constant);

constant = 5;
