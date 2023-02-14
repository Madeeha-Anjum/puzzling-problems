def solution(start, finish):
    # Find the minimum number of jumps to go from start to finish
    # cat can jump only 1 or 2 shelves up but not directly above itself

    # 1, 4, 7, -> 3 jumps to 7
    # 1,2,3,5,6,7 -> 7 jumps
    # 1 , 4 , 5, 6 ,7 -> 5 jumps
    # smallest is 3
    # always jump twice until you cannot

    count_jump = 0
    while start != finish:
        if start + 3 <= finish:
            start = start + 3
        else:
            start = start + 1
        count_jump = count_jump + 1
    return count_jump


def solution2(start, finish):
    n = finish - start
    return n // 3 + n % 3  # n//3 + remainder


if __name__ == "__main__":
    assert solution2(1, 5) == 2


#                  ┌────────┐
#                  │-6------│
#                  └────────┘
# ┌────────┐
# │------5-│
# └────────┘  ┌─────► OK!
#             │    ┌────────┐
#             │    │-4------│
#             │    └────────┘
# ┌────────┐  │
# │------3-│  │
# BANG!────┘  ├─────► OK!
#   ▲  |\_/|  │    ┌────────┐
#   │ ("^-^)  │    │-2------│
#   │ )   (   │    └────────┘
# ┌─┴─┴───┴┬──┘
# │------1-│
# └────────┘
