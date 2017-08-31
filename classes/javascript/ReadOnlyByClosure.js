#! /usr/bin/env node
"use strict";

function defineReadOnly(object, property, value){
  Object.defineProperty(object, property, {
    get: () => value
  });
}

class ObjectType {
  constructor(value){
    defineReadOnly(this, 'readonly1', value);
  }
}

const o = new ObjectType('hola');
console.log(o.readonly1);

defineReadOnly(o, 'readonly2', 'chau');
console.log(o.readonly2);

o.readonly1 = 'chau';
console.log(o.readonly1);
