import math


def cockroach_speed(s):
    """
    Input: speed in km /h -> real number aka rational and irrational
    Output: speed in cm/s (round to floor)
    Example:
     1.08km    1h     100,000cm
     ------ * ----- * ---------   = 30cm/s
       1 h    3600s      1km
    """

    converted = math.floor(s * (100000 / 3600))

    pass


if __name__ == "__main__":
    s = 1.08
    cockroach_speed(s)
