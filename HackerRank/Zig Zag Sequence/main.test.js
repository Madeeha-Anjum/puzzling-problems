const Solution = require('./main');

test('test the function', () => {
  expect(Solution.processData([2, 3, 5, 1, 4])).toBe('1,2,5,1,4');
});
