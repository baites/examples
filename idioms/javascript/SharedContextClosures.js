#! /usr/bin/env node
"use strict";

/**
 * Create two closures with share context
 * @param value - Value of context
 */
function CreateClosures(value) {
  let context = JSON.parse(
    JSON.stringify(value)
  );
  function GetMethod() {
    return JSON.parse(
      JSON.stringify(context)
    );
  }
  function SetMethod(value) {
    context = JSON.parse(
      JSON.stringify(value)
    );
  }
  return {
    'getContext': GetMethod,
    'setContext': SetMethod
  };
}

// Creating closures with protective share context
// Object mutability is irrelevant because context is
// protected by the closure (capture by copy and unreachable)
const closures = CreateClosures(['A']);

// Print original context value
console.log('get context value: ', closures.getContext());

// Set new context value
closures.setContext(['B']);
console.log('set and get context value: ', closures.getContext());

// It is not possible to get a refence to context
const context = closures.getContext();
context[0] = 'C';
console.log('get context value: ', closures.getContext());
