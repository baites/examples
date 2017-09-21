#! /usr/bin/env node
"use strict";

const CreateMethodWithContext = (value) => {
    const context = value;
    function Method() {
      return context;
    }
    return Method;
}

const origMethod = CreateMethodWithContext('origin value');
const newMethod = CreateMethodWithContext('new value');

console.log('context in orginal method: ' + origMethod());
console.log('context in new method: ' + newMethod());
