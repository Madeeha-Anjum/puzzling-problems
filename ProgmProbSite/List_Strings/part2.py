# https://adriann.github.io/programming_problems.html
from typing import Callable


def on_all(lst, func: Callable):
    # pass function ad arguments
    # for element in lst:
    #     # apply a function
    #     q8(element)
    # print(list(map(func, lst)))
    return list(map(func, lst))


def q8(element):
    #  print the first 20 perfect squares of the element
    # perfect squares of element
    #  take all the numbers from 1 to element and multiple to itself
    return element + 1


def q9(lst_a, lst_b):
    """Write a function that concatenates two lists. [a,b,c], [1,2,3] → [a,b,c,1,2,3]"""
    #  using extend
    # return [*lst_a, *lst_b]

    lst_a.extend(lst_b)

    return lst_a

    # OR


def q10(lst_a, lst_b):
    #  alternatively taking elements
    #  tale on and take another
    lst = []

    for i in range(0, len(lst_a)):
        lst.append(lst_a[i])
        lst.append(lst_b[i])

    return lst


def q11(lst_a, lst_b):
    #  merging 2 sorted lists
    lst = []
    # compare the first values of each and add to the new array
    for i in range(0, len(lst_a)):
        if lst_a[i] < lst_b[i]:
            lst.append(lst_a[i])
            lst.append(lst_b[i])
        else:
            lst.append(lst_b[i])
            lst.append(lst_a[i])

    return lst


if __name__ == "__main__":
    # --------------------------- Q8 ----------------------------
    # return perfect squares
    assert on_all([1, 5, 2, 6, 7, 3, 8, 9], q8)
    # --------------------------- Q9 ----------------------------
    #  Write a function that concatenates two lists.
    assert q9(["a", "b", "c"], [1, 2, 3]) == ["a", "b", "c", 1, 2, 3]
    # --------------------------- Q10 ----------------------------
    # Write a function that combines two lists by alternatingly
    assert q10(["a", "b", "c"], [1, 2, 3]) == ["a", 1, "b", 2, "c", 3]
    # --------------------------- Q11 ----------------------------
    # Merges two sorted lists into a new sorted list
    assert q11([1, 4, 6], [2, 3, 5]) == [1, 2, 3, 4, 5, 6]
