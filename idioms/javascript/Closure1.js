#! /usr/bin/env node
"use strict";

var context = 'method1 context';
function Method1(){
  return context;
}

function CreateMethod1() {
  var context = 'method1 context?';
  return Method1;
}

function CreateMethod2() {
    var context = 'method2 context';
    function Method2() {
      return context;
    }

    return Method2;
}

var method1 = CreateMethod1();
console.log(method1());

var method2 = CreateMethod2();
console.log(method2());
