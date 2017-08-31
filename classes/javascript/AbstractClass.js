class Base {
  constructor() {
    if (new.target === Base) {
      throw new TypeError("Cannot instanciate this class");
    }
    if (this.method === undefined) {
      throw new TypeError("Must override method");
    }
  }
}

class Derived1 extends Base {
  constructor() {
    super();
  }
}

class Derived2 extends Base {
  constructor() {
    super();
  }
  method(){
    return 'Method is implemented';
  }
}

//const b = new Base();
//const d1 = new Derived1();
const d2 = new Derived2();
console.log(d2.method())
