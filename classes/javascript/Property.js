class ObjectType {
  constructor(value){
    this._propname = value;
  }
  get propname() {
    console.log('getting propname');
    return this._propname;
  }
  set propname(value) {
    console.log('setting propname');
    this._propname = value;
  }
}

const o = new ObjectType('hola');
console.log(o.propname);

o.propname = 'chau';
console.log(o.propname);
