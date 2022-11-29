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
    assert.equal(solution.timeConversion('07:05:45PM'), '19:05:45');
  });
});
