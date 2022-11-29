const assert = require('chai').assert;

var Solution = function (arr) {};
/*
  Quicksort: comparison sorts | n 8 log(n)
  Counting sort: non-comparison sorts
      - create an integer arry 
      - count the number of times each integer occurs
      - output the number of times each integer occurs

  */

Solution.prototype.countingSort = function (arr) {
  let count_arr = new Array(arr.length).fill(0);

  for (let i = 0; i < arr.length; i++) {
    count_arr[arr[i]]++;
  }

  let sorted = [];

  for (let i = 0; i < count_arr.length; i++) {
    let size = count_arr[i];
    if (size > 0) {
      sorted.push(...new Array(size).fill(i));
    }
  }
  console.log(sorted.toString());
  return sorted.toString();
};

function main() {
  var solution = new Solution();
  console.log(`==== Here is start of the test ==== \n`);

  assert.equal(solution.countingSort([1, 1, 3, 2, 1]), '1,1,1,2,3');
}

main();
module.exports = new Solution();
