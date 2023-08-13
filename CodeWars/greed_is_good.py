"""
Greed is a dice game  
"""


def score(dice: list) -> int:
    """Returns the score of a dice roll according to the rules of Greed."""
    triplet_points = {
        1: 1000,
        6: 600,
        5: 500,
        4: 400,
        3: 300,
        2: 200,
    }
    single_points = {
        1: 100,
        5: 50,
    }
    points = 0

    rolls = dict((roll, dice.count(roll)) for roll in dice)

    points = 0
    for roll, occur in rolls.items():
        if occur >= 3:
            points += triplet_points[roll]
            occur -= 3
        if occur:
            if roll in single_points:
                points += single_points[roll] * occur

    return points


if __name__ == "__main__":
    assert score([5, 1, 3, 4, 1]) == 250
    assert score([1, 1, 1, 3, 1]) == 1100
    assert score([2, 3, 4, 6, 2]) == 0
    assert score([4, 4, 4, 3, 3]) == 400
    assert score([2, 4, 4, 5, 4]) == 450
