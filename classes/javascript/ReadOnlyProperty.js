#! /usr/bin/env node
"use strict";

class ObjectType {
  constructor(value){
    this._propname = value;
  }
  get propname() {
    return this._propname;
  }
}

const o = new ObjectType('hola');
console.log(o.propname);

o._propname = 'chau';
console.log(o.propname);

o.propname = 'chau';
console.log(o.propname);
