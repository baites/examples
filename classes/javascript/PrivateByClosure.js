#! /usr/bin/env node
"use strict";

class A {
  constructor(value){
    let counter = 0;
    this.tick = () => counter += 1;
    this.count = () => counter;
  }
}

const a = new A();
a.tick();
a.tick();
a.tick();
console.log(a.count());
