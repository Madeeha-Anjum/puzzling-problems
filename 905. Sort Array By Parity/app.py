from ntpath import join


class Solution:
    def sortArrayByParity(self, nums: list[int]) -> list[int]:
        """
        Input: array of ints
        Output: array of ints
        goal: move all even ints to the beginning

        """

        even = list(filter(lambda x: True if x % 2 == 0 else False, nums))
        odd = list(filter(lambda x: False if x % 2 == 0 else True, nums))
        res = even + odd

        return res


if __name__ == "__main__":
    nums = [3, 1, 2, 4]
    assert Solution().sortArrayByParity(nums) == [2, 4, 3, 1]
