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
    assert.equal(solution.lonelyinteger([1, 2, 3, 4, 3, 2, 1]), 4);
  });
});
