const assert = require('chai').assert;

var Solution = function () {};

Solution.prototype.lonelyinteger = function (arr) {
  // Write your code here

  let occurrence = {
    // value : count
  };
  for (let i = 0; i < arr.length; i++) {
    if (occurrence[arr[i]]) {
      occurrence[arr[i]]++;
    } else {
      occurrence[arr[i]] = 1;
    }
  }
  let max = null;
  Object.keys(occurrence).forEach((key) => {
    if (occurrence[key] === 1) {
      max = key;
    }
  });
  return max;
  // console.log(`occurrence: ${JSON.stringify(occurrence, null, 2)}`);

  // let max = 0;
  // // set the max occurrence

  // Object.keys(occurrence).forEach((key) => {
  //   if (occurrence[key] > max) {
  //     max = key;
  //   }
  // });

  // console.log('Here ', max);

  // // set the max occurrence
  // for (let [k, v] of Object.entries(occurrence)) {
  //   if (v > max) {
  //     max = k;
  //   }
  // }
  // console.log('Here ', max);

  // return max;
};

function main() {
  var solution = new Solution();
  console.log(`==== Here is start of the test ==== \n`);
  assert.equal(solution.lonelyinteger([1, 2, 3, 4, 3, 2, 1]), 4);
}

main();
module.exports = new Solution();
