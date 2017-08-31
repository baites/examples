
class Interface {
  constructor() {
    if (
      this.get === undefined || this.set === undefined
    ) {
        throw new TypeError("Must override method");
    }
  }
}

class Core extends Interface {
  constructor() {
    super();
    this.variable = null;
  }
  get() {
    return this.variable;
  }
  set(value) {
    this.variable = value;
    return value;
  }
  toString(){
    return `(${this.value})`
  }
}

class Decorator1 extends Interface {
  constructor(instance) {
    super();
    this.instance = instance;
  }
  get() {
    console.log('get method 1');
    return this.instance.get();
  }
  set(value) {
    console.log('put method 1');
    this.instance.set(value);
    return value;
  }
}

class Decorator2 extends Interface {
  constructor(instance) {
    super();
    this.instance = instance;
  }
  get() {
    console.log('get method 2');
    return this.instance.get();
  }
  set(value) {
    console.log('put method 2');
    this.instance.set(value);
    return value;
  }
}

const c = new Core();
c.set('hola')
console.log(c.get());

const d1 = new Decorator1(c);
d1.set('chau');
console.log(d1.get());

const d2 = new Decorator2(c);
d2.set('ultimo');
console.log(d2.get());
