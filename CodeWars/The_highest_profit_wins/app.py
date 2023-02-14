def min_max(lst):
    min, max = lst[0], lst[1]

    for num in lst:
        if num < min:
            min = num
        if num > max:
            max = num

    return [min, max]


if __name__ == "__main__":
    assert min_max([1, 2, 3, 4, 5]) == [1, 5]
