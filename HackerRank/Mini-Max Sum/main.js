const assert = require('chai').assert;

var Solution = function () {};

Solution.prototype.miniMaxSum = function (arr) {
  /*
  Find the min and max by summing exactly 4 of the 5 integers.
  */
  let min;
  let max;

  arr_max = Math.max(...arr);
  min = arr.reduce((a, b) => a + b) - arr_max;
  console.log('Here is min: ', min);

  arr_min = Math.min(...arr);
  max = arr.reduce((a, b) => a + b) - arr_min;
  console.log('Here is max: ', max);

  return `${min} ${max}`;

  //
};

function main() {
  var solution = new Solution();
  console.log(`==== Here is start of the test ==== \n`);

  assert.equal(solution.miniMaxSum([1, 3, 5, 7, 9]), '16 24');
}

main();
module.exports = new Solution();
