import itertools


def threeSum(nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]

    Input: array of numbers
    return [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k
    """
    #  O(n^3) - slow
    # three_sum = []

    # for i in range(len(nums)):
    #     for j in range(1, len(nums)):
    #         for k in range(2, len(nums)):
    #             if i != j and i != k and j != k and nums[i] + nums[j] + nums[k] == 0:
    #                 to_append = sorted([nums[i], nums[j], nums[k]])
    #                 if to_append not in three_sum:
    #                     three_sum.append(to_append)

    # three_sum = []
    # pointer_i = 0
    # pointer_j = 1
    # pointer_k = 2
    # num_size = len(nums) - 1

    # while pointer_i != num_size:
    #     print(pointer_i, pointer_j, pointer_k)

    #     if (
    #         pointer_i != pointer_j
    #         and pointer_i != pointer_k
    #         and pointer_j != pointer_k
    #         and nums[pointer_i] + nums[pointer_j] + nums[pointer_k] == 0
    #     ):
    #         print(":here")
    #         print()
    #         to_append = sorted([nums[pointer_i], nums[pointer_j], nums[pointer_k]])
    #         if to_append not in three_sum:
    #             three_sum.append(to_append)

    #     if pointer_k >= num_size:
    #         pointer_j += 1
    #         pointer_k = 2

    #     if pointer_j >= num_size:
    #         pointer_j = 1
    #         pointer_i += 1

    #     pointer_k += 1

    # print(three_sum)
    # return sorted(three_sum)

    # faster solution hash table
    # O(log n)
    # 1. sort the array
    # 2. iterate through the array
    # 3. for each element, find the other two elements that sum up to 0
    # 4. if the other two elements exist in the hash table, append to the result
    # 5. else, add the element to the hash table
    # 6. return the result

    # three_sum = []
    # nums.sort()

    # for i, j, k in itertools.combinations(range(len(nums)), 3):
    #     #  itertools is in C so its faster than list comprehension
    #     if i != j and i != k and j != k and nums[i] + nums[j] + nums[k] == 0:
    #         to_append = sorted([nums[i], nums[j], nums[k]])
    #         if to_append not in three_sum:
    #             three_sum.append(to_append)
    # return sorted(three_sum)

    nums.sort()
    result = []

    for i in range(len(nums) - 2):
        # Skip duplicates
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        left, right = i + 1, len(nums) - 1
        while left < right:
            curr_sum = nums[i] + nums[left] + nums[right]

            if curr_sum == 0:
                result.append([nums[i], nums[left], nums[right]])
                # Skip duplicates
                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1
                left += 1
                right -= 1
            elif curr_sum < 0:
                left += 1
            else:
                right -= 1

    return result


if __name__ == "__main__":
    assert threeSum([-1, 0, 1, 2, -1, -4]) == [[-1, -1, 2], [-1, 0, 1]]
    assert threeSum([0, 1, 1]) == []
    assert threeSum([0, 0, 0]) == [[0, 0, 0]]
    assert threeSum([1, -1, -1, 0]) == [[-1, 0, 1]]
