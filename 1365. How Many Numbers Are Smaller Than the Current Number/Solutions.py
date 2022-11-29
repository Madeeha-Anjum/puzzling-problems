class Solution:
    def smallerNumbersThanCurrent(self, nums):
        print(nums)

        output = []
        for i in nums:
            count = 0
            for j in nums:
                if j < i:
                    count += 1
            output.append(count)
        return output


print("Hello World")
Solution()  # instantiate the class
a = Solution()
nums = [8, 1, 2, 2, 3]
b = a.smallerNumbersThanCurrent(nums)
print(b)
