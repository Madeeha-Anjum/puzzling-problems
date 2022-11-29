# 1929. Concatenation of Array

In english:
- given `nums` with length n 
- create a 2n array where ans[i] == nums[i] and ans[i+n]==nums[i] for 0<=i< n


Example:

Input: nums = [1,2,1]
Output: [1,2,1,1,2,1]
Explanation: The array ans is formed as follows:
- ans = [nums[0],nums[1],nums[2],nums[0],nums[1],nums[2]]
- ans = [1,2,1,1,2,1]