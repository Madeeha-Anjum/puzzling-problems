"""
There rods are labeled 0-9

Input: 
    - string of 2n where n is the rings.  
    - color -position pair 
Return:
    - The number of rods that have all 3 colors of rings

"""


class Solution:
    def countPoints(self, rings: str) -> int:
        rod = {"0": [], "1": [], "2": [], "3": [], "4": [], "5": [], "6": [], "7": [], "8": [], "9": []}

        for i in range(len(rings)):
            # if the char is a number read the color before it
            # and place it inside the dictionary
            char = rings[i]
            if char in rod.keys():
                rod[char].append(rings[i - 1])

        # Find all keys that have BGR
        ans = []
        for key, values in rod.items():
            if "B" in values and "R" in values and "G" in values:
                ans.append(key)
        return len(ans)


rings = "B0B6G0R6R0R6G9"
solution = Solution()
ans = solution.countPoints(rings)
print(ans)
