def hoop_count(n):
    if n >= 10:
        return "Great, now move on to tricks"

    return "Keep at it until you get it"


if __name__ == "__main__":
    assert hoop_count(3), "Keep at it until you get it"
