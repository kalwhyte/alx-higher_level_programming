const Rectangle = require('./4-rectangle');

class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    if (!c) {
      c = 'X';
    }
    let square = '';
    for (let i = 0; i < this.height; i++) {
      square += c.repeat(this.width) + '\n';
    }
    console.log(square);
  }
}

module.exports = Square;
