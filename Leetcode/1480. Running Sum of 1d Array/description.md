* Given an array nums
running sum[i] = All the numbers from index 0 to i of the num array. 
aka runningSum[i] = sum(nums[0]…nums[i]).

* In english 
To get the current running sum we need to add up all of the 
previous numbers in the num array plus the current number. 

```Example
    Input: nums = [1,2,3,4]
    Output: [1,3,6,10]
    Explanation: Running sum is obtained as follows: [1, 1+2, 1+2+3, 1+2+3+4].
```

```constraints 
1 <= nums.length <= 1000
-10^6 <= nums[i] <= 10^6```