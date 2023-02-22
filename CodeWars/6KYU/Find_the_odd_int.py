def find_it(seq):
    # find the one that appears an odd number of times

    dic = {}

    for num in seq:
        if num in dic.keys():
            dic[num] = dic[num] + 1
        else:
            dic[num] = 1

    # find the odd value:
    for key, value in dic.items():
        if value % 2 != 0:
            return key


if __name__ == "__main__":
    assert find_it([20, 1, -1, 2, -2, 3, 3, 5, 5, 1, 2, 4, 20, 4, -1, -2, 5]) == 5
