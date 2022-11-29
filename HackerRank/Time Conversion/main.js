const assert = require('chai').assert;

var Solution = function () {};

Solution.prototype.timeConversion = function (str) {
  /*
     12 hour AM/PM format, convert it to military (24-hour) time.
  */
  if (str.slice(-2) === 'PM') {
    if (str.slice(0, 2) === '12') {
      return str.slice(0, 8);
    }
    return (parseInt(str.slice(0, 2)) + 12).toString() + str.slice(2, 8);
  }
  if (str.slice(-2) === 'AM') {
    if (str.slice(0, 2) === '12') {
      return '00' + str.slice(2, 8);
    }
    return str.slice(0, 8);
  }

  // // dose it need to be converted?
  // if (str.slice(-2) === 'AM' && str.slice(0, 2) === '12') {
  //   // 12:00:00AM on a 12-hour clock is 00:00:00
  //   return '00' + str.slice(2, 8); // Add string with a plus sign
  // }
  // if (str.slice(-2) === 'PM' && str.slice(0, 2) === '12') {
  //   return str.slice(0, 8);
  // }
  // if (str.slice(-2) === 'PM') {
  //   let time = parseInt(str.slice(0, 2)) + 12;
  //   return time + str.slice(2, 8);
  // }
  // if (str.slice(-2) === 'AM') {
  //   return str.slice(0, 8);
  // }
};

function main() {
  var solution = new Solution();
  console.log(`==== Here is start of the test ==== \n`);

  assert.equal(solution.timeConversion('07:05:45PM'), '19:05:45');
  assert.equal(solution.timeConversion('07:05:45PM'), '19:05:45');
}

main();
module.exports = new Solution();
