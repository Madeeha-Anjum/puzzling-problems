def lonelyinteger(str):
    """
    12 hour AM/PM format, convert it to military (24-hour) time.
    """
    if "AM" in str:
        print("AM")

        return


if __name__ == "__main__":

    assert lonelyinteger([1, 2, 3, 4, 3, 2, 1]) == 4
