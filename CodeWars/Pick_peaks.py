def pick_peaks(arr):
    """
    Input: arr[int]
    Output: {"pose" list[int], "peaks": list(int)}
    - a high is where the prev is lower than curr, and the next is lower than curr
    - edge case: if the same number is repeated its not a fail until the repation stops and you check
    """
    dic = {"pos": [], "peaks": []}
    if len(arr) < 3:
        return dic

    prev, curr, nxt = 0, 1, 2

    while nxt <= len(arr) - 1:
        if arr[prev] < arr[curr] and arr[curr] > arr[nxt]:
            dic.get("pos").append(curr)
            dic.get("peaks").append(arr[curr])

        if arr[prev] < arr[curr] and arr[curr] == arr[nxt]:
            nxt = nxt + 1  # increase next
            continue
        else:
            prev = curr  # increase prev
            curr = nxt  # increase curr
            nxt = nxt + 1  # increase next

    return dic


if __name__ == "__main__":
    assert (pick_peaks([1, 2, 3, 6, 4, 1, 2, 3, 2, 1])) == {
        "pos": [3, 7],
        "peaks": [6, 3],
    }

    assert pick_peaks(
        [1, 2, 5, 4, 3, 2, 3, 6, 4, 1, 2, 3, 3, 4, 5, 3, 2, 1, 2, 3, 5, 5, 4, 3]
    ) == {"pos": [2, 7, 14, 20], "peaks": [5, 6, 5, 5]}
