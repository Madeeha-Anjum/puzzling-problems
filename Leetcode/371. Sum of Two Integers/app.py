def get_sum(a, b):
    """
    :type a: int
    :type b: int
    :rtype: int
    Sum of the two integers without using the operators + and -.
    Input a = 1, b = 2
    Output: 3
    """
    a = bin(a)
    b = bin(b)
    a = a.lstrip("0b")
    a = a.replace("-0b", "")
    b = b.lstrip("0b")
    b = b.replace("-0b", "")
    max_len = max(len(a), len(b))
    a = a.zfill(max_len)
    b = b.zfill(max_len)

    result = ""
    carry = "0"

    for i in range(-1, -max_len - 1, -1):
        if a[i] == "0" and b[i] == "0":
            if carry == "1":
                result = "1" + result
                carry = "0"
            else:
                result = "0" + result
        elif a[i] == "1" and b[i] == "1":
            if carry == "1":
                result = "1" + result
                carry = "1"
            else:
                result = "0" + result
                carry = "1"
        else:
            if carry == "1":
                result = "0" + result
                carry = "1"
            else:
                result = "1" + result

    if carry == "1":
        result = "1" + result

    #  Todo: Add logic for negative numbers

    return int(result, 2)


if __name__ == "__main__":
    assert get_sum(1, 2) == 3
    assert get_sum(2, 3) == 5
    assert get_sum(20, 30) == 50
