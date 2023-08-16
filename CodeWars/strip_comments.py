"""
Strip Comments  
"""


def strip_comments(string, markers):
    """
    Input:
    apples, pears # and bananas
    grapes
    bananas !apples

    Output:
    apples, pears
    grapes
    bananas

    """
    solution = []
    for line in string.split("\n"):
        new_line = ""
        for letter in line:
            if letter in markers:
                break
            new_line += letter
        solution.append(new_line.rstrip())

    return "\n".join(solution)


if __name__ == "__main__":
    assert (
        strip_comments(
            "apples, pears # and bananas\ngrapes\nbananas !apples", ["#", "!"]
        )
        == "apples, pears\ngrapes\nbananas"
    )

    assert strip_comments("a #b\nc\nd $e f g", ["#", "$"]) == "a\nc\nd"
    assert strip_comments(" a #b\nc\nd $e f g", ["#", "$"]) == " a\nc\nd"
