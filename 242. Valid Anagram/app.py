class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """
        An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase,
        typically using all the original letters exactly once.
        """
        # take the letters away one by one and if there are letters left then it dosnt match
        # quickly match the length

        # for letter in list(s):
        #     if letter in list(t):
        #         t = t.replace(letter, "_", 1)

        # if t.count("_") == len(s):
        #     return True
        # else:
        #     return False

        if len(s) != len(t):
            return False

        for letter in list(t):
            if s.count(letter) != t.count(letter):
                return False

        return True


if __name__ == "__main__":
    s = Solution()
    print(s.isAnagram("anagram", "nagaram"))
