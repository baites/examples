
var recursion = function(s,l,c=[]){
  if (s.length === 0){
    if (c.length === 4){
      l.push(c);
      return true;
    }
    return false;
  }
  for(var n=1; n<4; ++n){
    p = c.slice();
    v = s.slice(0,n);
    if ((v.startsWith('0') && v.length > 1) || v > 255){
      continue;
    }
    p.push(v);
    if(recursion(s.slice(n),l,p)){
      break;
    }
  }
}

var initiator = function(s){
  l = [];
  recursion(s,l);
  for(var i=0; i<l.length; ++i){
    l[i] = l[i].join('.');
  }
  return l;
}

var ip = "255255255255";
console.log(ip + " -> [" + initiator(ip)+"]");
ip = "25525511255";
console.log(ip + " -> [" + initiator(ip)+"]");
ip = "25551125";
console.log(ip + " -> [" + initiator(ip)+"]");
ip = "2552";
console.log(ip + " -> [" + initiator(ip)+"]");
ip = "0255255255";
console.log(ip + " -> [" + initiator(ip)+"]");
ip = "0000";
console.log(ip + " -> [" + initiator(ip)+"]");
ip = "001100";
console.log(ip + " -> [" + initiator(ip)+"]");
ip = "001900";
console.log(ip + " -> [" + initiator(ip)+"]");
ip = "001994482909400";
console.log(ip + " -> [" + initiator(ip)+"]");
ip = "011";
console.log(ip + " -> [" + initiator(ip)+"]");
