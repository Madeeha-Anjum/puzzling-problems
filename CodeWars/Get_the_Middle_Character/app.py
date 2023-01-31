from math import ceil, floor


def get_middle(s):
    # given a word
    # return the middle char
    # odd-> return middle, even return 2 middle chr

    # how do i get the middle ?
    # start at the end and meet in the middle ? -> slower
    # just figure out the index of the middle one -> faster
    length = floor(len(s) / 2)
    return f"{s[length - 1 ]}{s[length]}" if (len(s) / 2) % 2 == 0 else s[length]


if __name__ == "__main__":
    assert get_middle("tes") == "e"
