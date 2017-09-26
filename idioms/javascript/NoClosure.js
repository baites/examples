#! /usr/bin/env node
"use strict";

// Defining context and method in global namespace
let context = 'A';

function Method() {
  return context;
}

/**
 * Create two closures with share context
 * @param value - Value of context
 */
function CreateMethodReference(value) {
  context = value;
  return Method;
}

// Print default initial context value
console.log('context when calling Method(): ' + Method());

// Create a reference to method and set context
const method = CreateMethodReference('B');
console.log('context when calling method: ' + method());
