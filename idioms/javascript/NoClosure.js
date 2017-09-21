#! /usr/bin/env node
"use strict";

let context = 'original value';
function Method(){
  return context;
}

function CreateMethodWithContext(value) {
  context = value;
  return Method;
}

const newMethod = CreateMethodWithContext('new value');

console.log('context in orginal method: ' + Method());
console.log('context in new method: ' + newMethod());
