def check(target: str, ano: str):
    if len(target) != len(target):
        return False
    target = list(target)
    ano = list(ano)
    res = list(filter(lambda x: ano.count(x) == target.count(x), target))
    if len(res) == len(target):
        return True
    else:
        return False


class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        """
        Input: Array of Strings (group of anagrams)
        Output: array of arrays of anagrams

        From the array of strings find which ones are anagrams
        Anagram: rearranged letters to create a new word

        put the anagrams together
        """

        my_dict = dict()

        while strs:
            print("list", strs)
            target = strs[0]
            my_dict[target] = [target]

            for key in strs[1:]:

                is_ano = check(target, key)
                if is_ano:
                    my_dict[target] += [key]

            # update strs

            for item in my_dict[target]:
                strs.remove(item)

        return list(my_dict.values())


if __name__ == "__main__":
    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    res = Solution().groupAnagrams(strs)
    print(res)


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        h = {}
        for word in strs:
            sortedWord = "".join(sorted(word))
            if sortedWord not in h:
                h[sortedWord] = [word]
            else:
                h[sortedWord].append(word)
        final = []
        for value in h.values():
            final.append(value)
        return final
