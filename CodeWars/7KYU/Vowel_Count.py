from functools import reduce


def get_count(sentence):
    # a,e,i,o, u
    return reduce(
        lambda count, letter: count + 1
        if letter in ["a", "e", "i", "o", "u"]
        else count,
        sentence,
        0,
    )

    # count = 0
    # for letter in sentence:
    #     if letter in ["a", "e", "i", "o", "u"]:
    #         count = count + 1
    # return count


if __name__ == "__main__":
    assert get_count("aeiou") == 5
