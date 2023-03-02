
# How many letters in the string 'stone' are also in 'jewels' when repeated letters count?

class Solution:
    # class variable shared by all instances go here

    def __init__(self):
        print("Class has been instantiated")

    # @staticmethod or we have to use self in the class mathod so its aware of its object class.
    # -> int: documents a return type
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        count = 0
        for element in stones:
            if element in jewels:
                count = count + 1
        return count


call = Solution()  # instansiate
ans = print(call.numJewelsInStones("aA", "aAAbbbb"))  # call method: return int
