def make_readable1(seconds):

    #  initialize
    hours, minutes, sec = 0, 0, 0

    if seconds >= 3600:
        hours = seconds // 3600

    if seconds % 3600 != 0:
        print(seconds % 3600)
        #  there are min
        minutes = (seconds % 3600) // 60

    if (seconds % 3600) % 60 != 0:
        print((seconds % 3600) % 60)
        # there are seconds
        sec = (seconds % 3600) % 60

    if hours < 10:
        hours = f"0{hours}"

    if minutes < 10:
        minutes = f"0{minutes}"

    if sec < 10:
        sec = f"0{sec}"

    # print(f"{hours}:{minutes}:{sec}")
    return f"{hours}:{minutes}:{sec}"


def make_readable2(seconds):

    hours, minutes, sec = 0, 0, 0

    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    sec = (seconds % 3600) % 60

    return f"{hours:02d}:{minutes:02d}:{sec:02d}"


if __name__ == "__main__":
    assert make_readable2(359999) == "99:59:59"
    assert make_readable2(0) == "00:00:00"
    assert make_readable2(5) == "00:00:05"
    assert make_readable2(60) == "00:01:00"
