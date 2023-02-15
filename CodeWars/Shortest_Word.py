from functools import reduce


def find_short(s):
    len_set = list(set(map(lambda x: len(x), s.split(" "))))

    # find smallest number in the set
    return reduce(lambda len, ans: ans if ans < len else len, len_set, len_set[0])


def find_short2(s):
    len_set = set(map(lambda x: len(x), s.split(" ")))

    len_set = [len(x) for x in s.split(" ")]

    # find smallest number in the set
    return min(len_set)


if __name__ == "__main__":
    assert find_short2("bitcoin take over the world maybe who knows perhaps") == 3
