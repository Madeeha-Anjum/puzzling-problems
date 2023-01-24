from functools import reduce


def grow(arr):
    return reduce(lambda a, b: a * b, arr)


if __name__ == "__main__":

    assert grow([1, 2, 3, 4]) == 24
