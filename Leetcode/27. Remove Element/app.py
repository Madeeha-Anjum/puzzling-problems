from typing import List


def removeElement(nums: List[int], val: int) -> int:
    """
    Input: array and a val
    Output array with val removed

    okay so replace all 3rd with "_"
    new Array = len old Array
    go though the old arr and keep adding the numbers and all extra space is "_"

    curr_filled_index = 0
    _  2  2  _
    👍

    move the number to current_index and replace old location with _
    curr_filled_index = 1
    2  _  2  _
       👍
    curr_filled_index = 1
     2  _  2  _
          👍
    curr_filled_index = 2
     2  2  _  _
          👍
    stop wien array ends

    """
    if not nums:
        return 0
    last_index = len(nums) - 1
    curr_pointer = 0

    while curr_pointer != last_index:
        if nums[curr_pointer] == val:
            # swap with last index
            nums[curr_pointer] = nums[last_index]
            nums[last_index] = val
            last_index -= 1
            # dont increase curr_pointer
        else:
            curr_pointer += 1

    return len(nums) - nums.count(val)


if __name__ == "__main__":
    nums1 = [3, 2, 2, 3]
    val = 3
    count = removeElement(nums1, val)
    print(
        "TEST 1: removed",
        val,
        "from the",
        nums1,
        "array",
        "count was",
        count,
        "end result",
        nums1[:count],
    )

    nums2 = [0, 1, 2, 2, 3, 0, 4, 2]
    val2 = 2
    count2 = removeElement(nums2, val2)
    print(
        "TEST 2: removed",
        val2,
        "from the",
        nums2,
        "array",
        "count was",
        count2,
        "end result",
        nums2[:count2],
    )
