var Solution = function () {};

Solution.prototype.processData = function (arr) {
  console.log(arr);
  k_elements = (arr.length + 1) / 2;
};

let solution = new Solution();
function main() {
  let input = [2, 3, 5, 1, 4];
  let result = solution.processData(input);
  console.log(result);
}

main();

module.exports = solution;
