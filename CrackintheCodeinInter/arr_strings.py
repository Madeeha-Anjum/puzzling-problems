from functools import reduce

def is_unique(s):
    # dose the string have all unique characters
    # dic = {}
    #  use a set became we only care about the key
    myset = set()

    for letter in s:
        if letter in myset:
            return False
        else:
            myset.add(letter)
    return True

    # for letter in s:
    #     if letter in dic:
    #         return False
    #     else:
    #         dic[letter] = 1
    # return True


def URLify(s, length):
    #  replace all space in a string with %20
    # print(s.strip().split(" "))
    # print(f'{"%20".join(s.strip().split(" "))}')
    return f'{"%20".join(s.strip().split(" "))}'


def check_permutation(s1, s2):
    # same letter different order
    # we should also sort both stings and compare if there the same 
    if len(s1) != len(s2):
        return False

    for letter in s1:
        if s2.count(letter) == 0:
            return False

    return True


def palindrome_permutation(s):
    #  can you make this string a palindrome

    s = s.replace(" ", "").lower()

    char_set1 = {}

    for letter in s:
        if letter in char_set1:
            char_set1[letter] += 1
        else:
            char_set1[letter] = 1
    print(char_set1)
    # if more than one count is 1 then its not a palindrome
    
    # for value in char_set1.values():
    #     lambda x : if x == 1 count++
    
    count = reduce(lambda acc, value : acc + 1  if value == 1 else acc,  char_set1.values(),0)
    return False if count == 2 else True 
    
    
    


if __name__ == "__main__":
    assert is_unique("sdkjfbshjdgqkbacn") == False

    assert URLify("Mr John Smith ", 13) == "Mr%20John%20Smith"

    assert check_permutation("ABC", "BAC") == True

    assert palindrome_permutation("taco cat") == True

    # assert string_rotation("waterbottle") == "erbottlewat"


 