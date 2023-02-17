# Given the triangle of consecutive odd numbers:

#              1
#           3     5
#        7     9    11
#    13    15    17    19
# 21    23    25    27    29


from functools import reduce


def row_sum_odd_numbers(n):
    """
    # sum of nth Row
    Example: row 3: 3 + 5
    start col -> 1,3,7,13 => add even each row 2,4,6. ->  even numbers = 2n
    numbers in row 7,9,11->add 2 each time max 3 numbers

    """
    col = [1]

    for i in range(1, n):
        col.append(col[-1] + 2 * i)

    row = [col[-1]]

    for i in range(n - 1):
        row.append(row[-1] + 2)

    # return reduce(lambda acc, num: acc + num, row, 0)
    return sum(row)


# or make a list of od and take the last n values
# Or just realize that the sum is n power  of 3 on each line


if __name__ == "__main__":
    assert row_sum_odd_numbers(2) == 8
    assert row_sum_odd_numbers(13) == 2197
    assert row_sum_odd_numbers(1) == 1
    assert row_sum_odd_numbers(19) == 6859
    assert row_sum_odd_numbers(41) == 68921
