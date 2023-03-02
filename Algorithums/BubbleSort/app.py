from sys import api_version


def bubble_sort(arr: list) -> list:
    """
    sorts smallest to largest
    1. compare the first 2 elements and move the largest right
    2. on the second instance we know the last one is the largest
    3. Stop when there is only 1 element left at the start aka no possibility of swapping
    """
    for i in range(len(arr) - 1):
        # don't compare the right most ordered
        size = len(arr) - 1 - i
        # swapping
        for j in range(size):
            if arr[j] > arr[j + 1]:
                temp = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = temp

    return arr


if __name__ == "__main__":
    arr = [8, 2, 1, 3, 10, 9, 5]
    print(arr)

    arr = bubble_sort(arr)
    print(arr)
