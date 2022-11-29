def plusMinus(arr):
    """
    Input: array of integers
    Output: ratio of pos, neg, zero to 6 decimal places
    """
    size_arr = len(arr)
    result_dict = {"pos": 0, "neg": 0, "zero": 0}

    for value in arr:
        if value > 0:
            result_dict["pos"] += 1
        if value < 0:
            result_dict["neg"] += 1
        if value == 0:
            result_dict["zero"] += 1
    result = list(
        map(lambda value: format(value / size_arr, "6f"), result_dict.values())
    )
    return result


if __name__ == "__main__":

    assert plusMinus([-4, 3, -9, 0, 4, 1]) == [0.500000, 0.333333, 0.166667]
