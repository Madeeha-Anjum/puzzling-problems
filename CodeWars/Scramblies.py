def scramble(s1, s2):
    # if s1 can be rearranged to match s2

    # gaol s2
    # rearrange s1 to make s2
    # return True if more than 3 letters match
    s1_dic = {}
    for val in s1:
        if val in s1_dic:
            s1_dic[val] += 1
        else:
            s1_dic[val] = 1

    #  now make s2
    match = ""
    for val in s2:
        if s1_dic.get(val):
            s1_dic[val] -= 1
            match += val
        else:
            return False

    if s2.count(match) == 1:
        return True

    return False


if __name__ == "__main__":
    assert scramble("rkqodlw", "world") == True
    assert scramble("cedewaraaossoqqyt", "codewars") == True
    assert scramble("katas", "steak") == False
    assert scramble("jscripts", "javascript") == False
    assert scramble("ljwdlebogrjavz", "jbwzlrbalje") == False
