from functools import reduce


def hash(item):
    # convert to list of numbers

    return reduce(lambda acc, value: acc + ord(value), list(item), 0)


def my_hash_map(list_of_strings):
    """
    Input: list of strings
    Put them in a hashmap
    Create hash based on sum_of_char (ASCII)
    Return dic with hashes as keys
    """
    dic = dict()
    for item in list_of_strings:
        # convert to hash
        dic[hash(item)] = [item]

    return dic


if __name__ == "__main__":
    print("hello")
    assert my_hash_map(["alphabet"]) == {833: ["alphabet"]}
    assert my_hash_map(
        ["alphabet", "black", "bAFLoyJJzA9SM5V", "SySnJ3qRxZagl2D", "XzCGL6oIxNWvmmo"]
    ) == {
        833: ["alphabet"],
        509: ["black"],
        1232: ["bAFLoyJJzA9SM5V"],
        1353: ["SySnJ3qRxZagl2D"],
        1394: ["XzCGL6oIxNWvmmo"],
    }
