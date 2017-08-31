var Point = (function(){
  function Point(x, y) {
    this.x = x;
    this.y = y;
  };
  Point.prototype.toString = function(){
    return `(${this.x}, ${this.y})`;
  }
  return Point
}())

var ColorPoint = (function(){
  function ColorPoint(x, y, color) {
    Point.call(this, x, y);
    this.color = color;
  }
  ColorPoint.prototype = Object.create(Point.prototype);
  ColorPoint.prototype.constructor = ColorPoint;
  ColorPoint.prototype.toString = function() {
    var p = new Point(this.x, this.y).toString();
    return p + ' in ' + this.color;
  }
  return ColorPoint;
}())

var cp = new ColorPoint(1, 2, 'red');
console.log(cp.toString());
