# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        tmp = ListNode(0, head)
        fast = tmp
        slow = tmp

        # move the fast n + 1 times
        for _ in range(n + 1):
            fast = fast.next


        # move both fast and slow 
        while fast:
            slow = slow.next
            fast = fast.next

        # removal
        slow.next = slow.next.next

        return tmp.next

       
