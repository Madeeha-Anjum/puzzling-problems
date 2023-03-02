class Solution:
    def reverseString(self, s: list[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        # s[0] = s[len(s) - 1]
        # s[1] = s[len(s) - 2]
        # s[2] = s[len(s) - 3]

        # stop if s[x] = s[len(s)- x]
        #     return s
        end = len(s) - 1
        for i in range(len(s)):
            # return the solution
            if i == end - i or i > end - i:
                return s

            # swap values
            temp = s[i]
            s[i] = s[end - i]
            s[end - i] = temp


if __name__ == "__main__":
    s = ["h", "e", "l", "l", "o"]
    Solution().reverseString(s)
    print(s)

    s = ["H", "a", "n", "n", "a", "h"]
    Solution().reverseString(s)

    print(s)
