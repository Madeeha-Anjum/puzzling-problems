from typing import List


def merge(arr1: List[int], m: int, arr2: List[int], n: int) -> None:
    """
    Do not return anything, modify nums1 in-place instead.

             👎
     4   5   6   0   0   0
     1   2   3
            👍
         👎
     4   5  6   0   0   6
     1   2  3
           👍
    👎
     4   5  6   0   5   6
     1   2  3
           👍

    # this pointer is no longer active
     4   5  6   4   5   6
     1   2  3
           👍

     4   5  3    4   5   6
     1   2  3
         👍

     4   2  3    4   5   6
     1   2  3
     👍

     1   2  3   4   5   6
     1   2  3
     👍

    """
    pointer_arr1 = m - 1
    pointer_arr2 = n - 1
    position = m + n - 1

    while pointer_arr1 >= 0 and pointer_arr2 >= 0:
        if arr1[pointer_arr1] > arr2[pointer_arr2]:
            arr1[position] = arr1[pointer_arr1]
            pointer_arr1 -= 1
            position -= 1
        else:
            arr1[position] = arr2[pointer_arr2]
            pointer_arr2 -= 1
            position -= 1

    # if there is still and arr2
    while pointer_arr2 >= 0:
        arr1[position] = arr2[pointer_arr2]
        pointer_arr2 -= 1
        position -= 1

    return arr1


if __name__ == "__main__":
    assert merge([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3) == [1, 2, 2, 3, 5, 6]
    assert merge([1], 1, [], 0) == [1]
    assert merge([4, 5, 6, 0, 0, 0], 3, [1, 2, 3], 3) == [1, 2, 3, 4, 5, 6]
