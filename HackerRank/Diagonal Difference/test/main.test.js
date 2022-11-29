const assert = require('chai').assert;
let Solution = require('../main');

describe('Basic Test', () => {
  it('should correctly answer 1 + 1', () => {
    assert.equal(1 + 1, 2);
  });
});

describe('main test', function () {
  let solution = Solution;

  it('check the function', function () {
    let items = [
      [11, 2, 4],
      [4, 5, 6],
      [10, 8, -12],
    ];
    assert.equal(solution.diagonalDifference(items), '15');
  });
});
