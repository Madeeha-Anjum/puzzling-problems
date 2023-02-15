def set_alarm(employed, vacation):
    """
    return true if you are employed and not on vacation
    return false otherwise
    """

    if employed and not vacation:
        return True
    else:
        return False


if __name__ == "__main__":
    assert set_alarm(True, True) == False
