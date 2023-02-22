def array_diff(a, b):
    # your code here
    """
    remove all values from list a, which are present in list b keeping their order.
    """
    # list union list b list a - union

    return list(filter(lambda a_val: a_val not in b, a))


if __name__ == "__main__":
    assert array_diff([1, 2], [1]) == [2]
    assert array_diff([1, 2, 2, 2, 3], [2]) == [1, 3]
