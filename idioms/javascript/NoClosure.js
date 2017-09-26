#! /usr/bin/env node
"use strict";

// Defining context and method in global namespace
let context = 'A';
function Method() {
  return context;
}

function CreateMethodWithContext(value) {
  context = value;
  return Method;
}

// Print default initial context value
console.log('context when calling Method(): ' + Method());

// Create a reference to method and set context
const method = CreateMethodWithContext('B');
console.log('context when calling method: ' + method());
