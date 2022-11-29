const assert = require('chai').assert;

var Solution = function () {};

Solution.prototype.diagonalDifference = function (arr) {
  /* Write your code here
    takes in a square matrix n*n
    return  sum both diagonals take there absolute difference
  */
  // how deep we need to go
  let square = arr.length;
  let primary = 0;
  let secondary = 0;

  // primary diagonal
  for (let i = 0; i < square; i++) {
    console.log(square, i);
    primary += arr[i][i];
    console.log('Here is primary', primary, arr[i][i]);
  }
  console.log(primary);

  // secondary diagonal
  for (let i = 0; i < square; i++) {
    secondary += arr[i][square - i - 1];
  }

  return Math.abs(primary - secondary);
};

function main() {
  var solution = new Solution();
  console.log(`==== Here is start of the test ==== \n`);

  let items = [
    [11, 2, 4],
    [4, 5, 6],
    [10, 8, -12],
  ];
  assert.equal(solution.diagonalDifference(items), '15');
}

main();
module.exports = new Solution();
