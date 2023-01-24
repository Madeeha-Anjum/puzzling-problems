from functools import reduce


def sum_mix1(arr):
    n_arr = []
    for i in arr:
        if type(i) == str:
            n_arr.append(int(i))
        else:
            n_arr.append(i)
    return reduce(lambda a, b: a + b, n_arr)


# another way
def sum_mix2(arr):
    return sum(map(int, arr))


#  another way
def sum_mix3(arr):

    return sum(int(i) for i in arr)


if __name__ == "__main__":

    ans = sum_mix1([9, 3, "7", "3"])  # ans  = 22
    print(ans)
