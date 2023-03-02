# https://adriann.github.io/programming_problems.html
from math import floor
from time import sleep


def q1(lst):
    largest = lst[0]
    for num in lst:
        if num > largest:
            largest = num
    return largest


# def q1(lst):
#     return max(lst)


# def q2(lst) -> list[int]:
#     lst.reverse()  # change the original -> reverse in place
#     return lst


def q2(lst):

    for i in range(len(lst)):
        # if i == floor(len(lst) / 2):
        if i == len(lst) // 2:
            # stop swapping when the middle is reached
            break
        # swap first and last
        temp = lst[len(lst) - 1 - i]
        lst[len(lst) - 1 - i] = lst[i]
        lst[i] = temp

    return None


# def q3(element, lst):
#     if lst.count(element) >= 1:
#         return True
#     else:
#         return False


def q3(element, lst):
    for i in lst:
        if i == element:
            return True
    return False


def q4(lst):
    # [item for idx, item in enumerate(lst) if idx % 2 != 0]
    #  returns the elements on odd positions in a list
    # 1,3,5,7,9
    res = []
    for i in range(len(lst)):
        # if i is even: skip
        if i % 2 == 0:
            continue
        res.append(lst[i])

    return res


def q5(lst):
    # running total
    # at 0 add 0
    # at 1 add 1 and 0
    # add all the previous
    res = []
    sum = 0
    for i in lst:
        sum = sum + i
        res.append(sum)
    print(res)
    return res


def q6(input):
    # reads the same backwards
    # turn to list
    # give to q2
    # if list == q2 return true
    # split the string at its spaces, join it and make it lower case
    input = list("".join(input.split()).lower())

    # reverse = [*input]  # create a new array
    # reverse.reverse() # reverse in place
    # or
    reverse = list(reversed(input))  # dont revers in place

    for r, i in zip(reverse, input):
        if r != i:
            return False
    return True


def q7a(lst):
    # for loop
    sum = 0
    for i in lst:
        sum = sum + i
    return sum


def q7b(lst):
    # while loop
    sum, i = 0, 0

    while i < len(lst):
        sum = sum + lst[i]
        i = i + 1

    return sum


def q7c(lst, sum=0):
    # recursion
    if len(lst) == 0:
        return sum

    sum = sum + lst[0]
    return q7c(lst[1:], sum)


if __name__ == "__main__":
    # --------------------------- Q1 ----------------------------
    # return the largest element in the list
    assert q1([2, 7, 4, 3, 5, 1, 9, 8, 10]) == 10

    # --------------------------- Q2 ----------------------------
    # reverses a list, preferably in place
    assert q2([7, 4, 3, 5, 1, 9, 8, 2]) == None

    # --------------------------- Q3 ----------------------------
    # checks whether an element occurs in a list
    assert q3(3, [1, 2, 4, 5, 10, 9, 6, 3]) == True
    assert q3(1, [4, 10, 6, 7, 8, 3, 2]) == False

    # --------------------------- Q4 ----------------------------
    #  returns the elements on odd positions in a list
    assert q4([2, 7, 4, 3, 5, 1, 9, 8, 10]) == [7, 3, 1, 8]

    # --------------------------- Q5 ----------------------------
    # the running total of a list
    assert q5([2, 7, 4, 3, 5, 1, 9, 8, 10]) == [2, 9, 13, 16, 21, 22, 31, 39, 49]

    # --------------------------- Q6 ----------------------------
    # tests whether a string is a palindrome(reads the same forwards and backwards)
    assert q6("A man a plan a canal Panama") == True

    # --------------------------- Q7 ----------------------------
    # 3 functions Sum of the numbers in a list -> for-loop, a while-loop and recursion
    assert q7a([2, 7, 4, 3, 5, 1, 9, 8, 10]) == 49  # for-loop
    assert q7b([2, 7, 4, 3, 5, 1, 9, 8, 10]) == 49  # while-loop
    assert q7c([2, 7, 4, 3, 5, 1, 9, 8, 10]) == 49  # recursion
