def abbrev_name(name):
    #
    f, l = name.split(" ")
    return ".".join([f[0].upper(), l[0].upper()])


if __name__ == "__main__":
    assert abbrev_name("Sam Harris") == "S.H"
