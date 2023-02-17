# "{}/{}".format() is helpful
from functools import reduce


def printer_error1(s):
    # aaabbbbhaijjjm -> printer used 3 times color a and ect...
    # return errors/length of string
    # errors include letters not in a to m
    # convert to ASCII and see if any of the numbers are between 110 and 122

    lst = list(map(lambda x: ord(x), s))
    dic = {}
    for num in lst:
        if num in dic:
            dic[num] = dic[num] + 1
        else:
            dic[num] = 1
    # find how many are between 110 and 122
    err = 0
    for key, item in dic.items():
        if key > 110:  # ord('n')
            err = err + dic[key]

    return str(err) + "/" + str(len(s))


def printer_error2(s):
    lst = list(map(lambda x: ord(x), s))
    dic = {}
    for num in lst:
        if num in dic:
            dic[num] = dic[num] + 1
        else:
            dic[num] = 1
    return (
        str(
            reduce(
                lambda acc, item: acc + item[1] if item[0] >= 110 else acc,
                dic.items(),
                0,
            )
        )
        + "/"
        + str(len(s))
    )


def printer_error3(s):
    err = 0
    for letter in s:
        if letter > "m":
            err = err + 1
    print(f"{err}/{len(s)}")
    print("{}/{}".format(err, len(s)))
    return f"{err}/{len(s)}"


def printer_error(s):
    return f"{ reduce(lambda acc, s: acc + 1 if ord(s) >= 110 else acc,s,0,)}/{len(s)}"


if __name__ == "__main__":
    s = "aaaaaaaaaaaaaaaabbbbbbbbbbbbbbbbbbmmmmmmmmmmmmmmmmmmmxyz"
    assert printer_error(s) == "3/56"
