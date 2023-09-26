# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        -👌= prev
        -👍= curr
        -✌️= next
        
        prev = null
        curr = 1
        next = 2
        null   1  - > 2  - > 3  - > 4  - > 5
        👌     👍   ✌️
        
        #  curr pointer points to prev
        curr = 2
        prev = 1
        next = 3
        null  <- 1  - > 2  - > 3  - > 4  - > 5
                👌     👍    ✌️
                
        #  make the curr pointer point to prev
        curr = 3
        prev = 2
        next = 4
        null  <- 1  < -  2  - > 3  - > 4  - > 5
                       👌     👍     ✌️
        """
        #     create pointers
        prev = None
        curr = head

        while curr:
            tmp = curr.next
            # make the current pointer point backwards
            curr.next = prev
            #  assign prev pointer to curr
            prev = curr
            #  assign current pointer to next
            curr = tmp

        return prev


if __name__ == "__main__":
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, None)))))
    assert Solution().reverseList(head)
