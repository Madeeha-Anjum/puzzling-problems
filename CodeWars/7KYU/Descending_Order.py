def descending_order1(num):

    # swapping method
    num = str(num)
    num = [int(x) for x in str(num)]

    if len(num) == 1:
        print(int("".join([str(x) for x in num])))
        return int("".join([str(x) for x in num]))

    # go through the list swap the values is right is smaller

    while True:
        has_swapped = False
        for i in range(1, len(num)):
            if num[i - 1] < num[i]:
                # swap
                has_swapped = True
                temp = num[i - 1]
                num[i - 1] = num[i]
                num[i] = temp
        if not has_swapped:
            break

    return int("".join([str(x) for x in num]))


def descending_order(num):
    num = str(num)
    num = [int(x) for x in str(num)]

    # what is sorted

    return int("".join(str(x) for x in sorted(num, reverse=True)))


if __name__ == "__main__":
    # assert descending_order(0) == 0
    assert descending_order(42145) == 54421
