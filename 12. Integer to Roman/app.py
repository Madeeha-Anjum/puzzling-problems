"""
Input: integer  
Output: Roman Numeral 
I, V, X, L, C, D, M = 1, 5, 10, 50, 100, 500, 1000

Rules: 
Example1: II is 1 + 1 = 2
Example2: XII is 10 + 1 + 1 = 12

Roman numerals are usually written largest to smallest 
If there written smallest first then its subtraction
Example3: 4 = IV = 5 - 1 
Example4: 6 = VI = 5 + 1

"""


class Solution:
    def intToRoman(self, num: int) -> str:

        legend = {
            1: "I",
            4: "IV",
            9: "IX",
            5: "V",
            10: "X",
            40: "XL",
            50: "L",
            90: "XC",
            100: "C",
            400: "CD",
            500: "D",
            900: "CM",
            1000: "M",
        }
        target = num
        roman = ""
        while target > 0:
            # find closest value in legend to target
            closest = list(filter(lambda x: x <= target, legend.keys()))
            # closest = min(legend.keys(), key=lambda k: abs(k - target))
            # Store the Roman numerical

            roman = roman + legend[max(closest)]
            target = target - max(closest)

        return roman


if __name__ == "__main__":

    assert Solution().intToRoman(58) == "LVIII"
