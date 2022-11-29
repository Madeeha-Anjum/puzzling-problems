def is_anagram(word1, word2):
    if len(word1) != len(word2):
        return False

    for letter in list(word1):
        # see if all letters of current word1 are in word2
        if word1.count(letter) != word2.count(letter):
            return False

    return True


class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        """
        Input: Array of Strings (group of anagrams)
        Output: array of arrays of anagrams

        From the array of strings find which ones are anagrams
        Anagram: rearranged letters to create a new word

        """

        myDic = {}

        for word in strs:

            letter_count = {}
            for letter in list(word):
                letter_count[letter] = word.count(letter)

            if letter_count in myDic.keys():
                print(f"{word} is already in dic")
            else:
                print(f"add new word: {word} to dic")
        pass


if __name__ == "__main__":
    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    res = Solution().groupAnagrams(strs)
    print(res)


# Problem: you have an inner and outer loop, but you want to break / continue in the outer loop based on a condition in the inner loop
# Solutions:
# 1) Use a flag which is created in the outer loop, modified in the inner loop and based on this flag, the outer loop does something
# 2) Create a new function, put the inner loop in that function, return some value. The outer loop calls the function and does something based on the return value
# 3) Restructure the logic so that you don't have this problem. Example: using all() or any() or map()

# 1)

# target = strs[0]
# rest = strs[1:]

# res = []

# print("Target:", target)
# print("Rest:", rest)

# for word in rest:
#     # is_ano = False

#     # check if its an anagram of target
#     # if it is, add it to res

#     is_anagram = True

#     if len(word) != len(target):
#         is_anagram = False

#     for letter in list(word):
#         # see if all letters of current word are in target
#         if word.count(letter) != target.count(letter):
#             is_anagram = False
#             break

#     if is_anagram:
#         res.append(word)

# print("result", res)

# pass

# 2)

# def is_anagram(word1, word2):
#     if len(word1) != len(word2):
#         return False

#     for letter in list(word1):
#         # see if all letters of current word1 are in word2
#         if word1.count(letter) != word2.count(letter):
#             return False

#     return True

# 3)

#    if list(map(lambda letter: word.count(letter), list(word))) == list(
#                 map(lambda letter: word.count(letter), list(target))
#             ):
#                 res.append(word)
