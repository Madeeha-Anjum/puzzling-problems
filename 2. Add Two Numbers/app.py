from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    @staticmethod
    def createListNode(nodes: list) -> ListNode:
        root = ListNode(nodes[0])  # save the root

        head = root
        for node in nodes[1:]:
            head.next = ListNode(node)
            head = head.next  # update the new head

        return root

    @staticmethod
    def ListNodeToList(head: ListNode) -> list[int]:
        nodes = []
        while head is not None:
            nodes.append(head.val)
            head = head.next

        return nodes

    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        """
        Input: l1 = [2,4,3], l2 = [5,6,4]
        Output: [7,0,8]
        Explanation: 342 + 465 = 807
        """
        l1 = type(self).ListNodeToList(l1)
        l1.reverse()
        l1 = int("".join([str(i) for i in l1]))
        # l1 = Solution.ListNodeToList(l1)
        l2 = Solution.ListNodeToList(l2)
        l2.reverse()
        l2 = int("".join([str(i) for i in l2]))

        added = list(map(int, str(l1 + l2)))
        added.reverse()
        added = Solution.createListNode(added)

        return added


if __name__ == "__main__":
    # Create ListNodes and print
    l1 = Solution.createListNode([2, 4, 3])
    print(Solution.ListNodeToList(l1))
    l2 = Solution.createListNode([5, 6, 4])
    print(Solution.ListNodeToList(l2))
    # add ListNodes
    solution = Solution()  # self means instance
    ans = solution.addTwoNumbers(l1, l2)
    print(Solution.ListNodeToList(ans))
