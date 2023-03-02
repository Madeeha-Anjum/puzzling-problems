
import itertools


class Solution:

    # def twoSum(self, nums: list[int], target: int) -> list[int]:

    #     for i in range(len(nums)):
    #         for j in range(i+1,len(nums)):
    #             if i != j and nums[i] + nums[j] == target:
    #                 return [i, j]
    #
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        for i, j in itertools.combinations(range(len(nums)), 2):
            #  itertools is in C so its faster than list comprehension
            if i != j and nums[i] + nums[j] == target:
                return [i, j]


if __name__ == '__main__':

    solution = Solution().twoSum([3, 2, 4], 6)
    print(solution)
