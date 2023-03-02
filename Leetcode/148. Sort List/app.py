from tkinter.tix import Tree
from typing import Optional

# Definition for singly-linked list.
# In Singly Linked Lists each node points to only the next node.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    # The self means this is an instance method, So to use you need to create an instance
    def sort_list(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Given the head of a linked list, return the list after sorting it in ascending order.
        Using Bubble sort
        A faster way would be: merge sort !!!!!! or
            [ListNode(1,next), Listndoe(2,next)]

            sort([1,2,3] key = lambda node: node.val)

            [ListNode(1,next), Listndoe(2,next)]

        """
        if head is None:
            return None
        head_pointer = head  # reset the head
        stop = True
        while head_pointer.next is not None:
            if head_pointer.val > head_pointer.next.val:  # swap values
                temp = head_pointer.val
                head_pointer.val = head_pointer.next.val
                head_pointer.next.val = temp
                stop = False  # if values are swapped we are not done

            head_pointer = head_pointer.next

        print_linked_list(head)  # print the largest value at the end

        # stop condition for sorting
        if stop is True:
            return head
        return self.sort_list(head)  # recursive call


def print_linked_list(head: ListNode, vals: Optional[list[int]] = None) -> None:
    if vals is None:
        vals = []

    vals.append(head.val)  # save the current node value

    if head.next is None:  # if there is no next head -> stop
        print("->", vals)
        return

    head = head.next  # set a new head to the next node
    print_linked_list(head, vals)  # loop again with the node values list


def find_in_linked_list(head, val) -> Optional[ListNode]:

    while head is not None and head.val != val:  # executes the code until the statement is met
        head = head.next

    return head


def remove_duplicates(head: ListNode):
    """
    Make a new Linked list add one item at a time;
    while traversing check if the value already exists
    if it exists don't add it to the new linked list
    """
    head_dr: ListNode = ListNode(5)  # new ListNode

    while head is not None:
        if find_in_linked_list(head_dr, head.val):
            head = head.next
            continue
        add_to_ListNode(head_dr, ListNode(head.val))
        head = head.next  # updates

    return head_dr


def add_to_ListNode(head, node: ListNode) -> None:
    while True:
        if head.next is None:
            head.next = node
            break
        head = head.next


def create_linked_list(arr: list) -> Optional[ListNode]:
    """
    # ListNode(list[0], ListNode(list[1],...))
    """
    if not arr:  # none or empty
        return

    head = ListNode(arr[0])
    arr = arr[1:]
    for i in arr:
        add_to_ListNode(head, ListNode(i))

    return head
    # The O(n) way instead of the O(n^2) way
    # prevListNode = ListNode(arr[0])
    # for i in arr:
    #     currentListNode = ListNode(i, prevListNode)
    #     prevListNode = currentListNode


if __name__ == "__main__":
    # heads = [5, 2, 1, 3]
    """
    Creating
    -> head = ListNode(5, ListNode(2, ListNode(2, ListNode(3))))
    """
    print("Creating...")
    head = create_linked_list([8, 2, 1, 3, 1, 2, 5, 4])
    print_linked_list(head)

    """"
    Find in listNode
    """
    print("Finding in ListNode...")

    ans = find_in_linked_list(head, 3)
    print(ans.val) if ans else print("None")

    """
    Removing duplicates 
    """
    print("Removing the duplicates in ListNode...")

    add_to_ListNode(head, ListNode(5, ListNode(3, ListNode(1))))
    head = remove_duplicates(head)
    print_linked_list(head)

    """
    Sorting 
    """
    print("Sorting ListNode...")
    head = create_linked_list([4, 2, 1, 3])

    solution = Solution()
    solution.sort_list(head)
    print_linked_list(head)
