from heapq import merge
from tabnanny import check


class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        """
        Merge the over lapping intervals
        [1, 3], [2, 6] become [1,6]
        """
        intervals.sort(key=lambda x: x[0])  # sort by the first element of the list
        i = 0
        j = 1
        size = len(intervals) - 1
        merged = []
        while True:
            print(i, j)

            if i > size:
                break
            if j > size:
                merged.extend([intervals[i]])
                break

            pointer = intervals[i]
            next = intervals[j]

            if pointer[1] >= next[0] and pointer[1] <= next[1]:
                # add new array to merged
                # increase pointer
                # increase next by 2
                i += 2
                j += 2
                merged.extend([[pointer[0], next[1]]])
            else:
                i += 1
                j += 1
                merged.extend([pointer])

        return merged


if __name__ == "__main__":
    s = Solution()
    print(s.merge([[1, 3], [2, 6], [8, 10], [15, 18]]))
