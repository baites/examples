#! /usr/bin/env node
"use strict";

function readonly(object, name, value){
  Object.defineProperty(object, name, {
    get: () => value
  });
}

function A() {
  readonly(this, 'constant', 'constant value');
}
const a = new A();
console.log(a.constant);

readonly(global, 'constant', 'global constant value');
console.log(constant);

constant = 5;
