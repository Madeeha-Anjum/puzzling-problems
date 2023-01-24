def count_by(x, n):
    """
    Return a sequence of numbers counting by `x` `n` times.
    """
    lst = range(1, n + 1)

    return list(map(lambda num: num * x, lst))


if __name__ == "__main__":
    assert count_by(1, 10) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    assert count_by(2, 5) == [2, 4, 6, 8, 10]
