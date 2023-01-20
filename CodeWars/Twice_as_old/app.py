import math


def twice_as_old(dad_years_old, son_years_old):
    """
    how many years ago the father was twice as old as his son
    (or in how many years he will be twice as old).
    """

    twice_as_old = son_years_old * 2
    return abs(dad_years_old - twice_as_old)


if __name__ == "__main__":
    assert twice_as_old(36, 7) == 22
