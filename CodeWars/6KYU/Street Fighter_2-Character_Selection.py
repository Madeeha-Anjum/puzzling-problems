def street_fighter_selection(fighters, initial_position, moves):
    # A  2x6 grid of fighters,
    # Return a list of fighters that were hovered over
    # if the end is reached it loops over
    # starts at the top left

    # keep a list of indexes that have been for every move
    index = [initial_position[0], initial_position[1]]
    touched = []
    for move in moves:

        if move == "left":

            if index == [index[0], 0]:
                # if it hits the left end rotate over
                index = [index[0], 6]
            index = [index[0], index[1] - 1]

        if move == "right":
            if index == [index[0], 5]:
                # if it hits the right end rotate over
                index = [index[0], -1]
            index = [index[0], index[1] + 1]

        if move == "up":
            # if there is nothing above update to itself
            if index[0] == 1:
                index = [index[0] - 1, index[1]]

        if move == "down":
            # if there is nothing above update to itself
            if index[0] == 0:
                index = [index[0] + 1, index[1]]

        touched.append(fighters[index[0]][index[1]])

    return touched


if __name__ == "__main__":
    fighters = [
        ["Ryu", "E.Honda", "Blanka", "Guile", "Balrog", "Vega"],
        ["Ken", "Chun Li", "Zangief", "Dhalsim", "Sagat", "M.Bison"],
    ]
    moves = []
    assert street_fighter_selection(fighters, (0, 0), moves) == []

    moves = ["left"] * 8
    print(moves)
    assert street_fighter_selection(fighters, (0, 0), moves) == [
        "Vega",
        "Balrog",
        "Guile",
        "Blanka",
        "E.Honda",
        "Ryu",
        "Vega",
        "Balrog",
    ]

    moves = ["up"] * 4

    assert street_fighter_selection(fighters, (0, 0), moves) == [
        "Ryu",
        "Ryu",
        "Ryu",
        "Ryu",
    ]
    moves = ["up", "left", "down", "right"] * 2
    assert street_fighter_selection(fighters, (0, 0), moves) == [
        "Ryu",
        "Vega",
        "M.Bison",
        "Ken",
        "Ryu",
        "Vega",
        "M.Bison",
        "Ken",
    ]
