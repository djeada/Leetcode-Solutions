# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if head is None or head.next is None or head.next.next is None:
            return

        # split the list
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast =  fast.next.next

        # reverse the second part
        second = slow.next
        slow.next = None
        curr = second
        prev = None
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        # merge
        first = head
        second = prev

        while second:
            tmp_first = first.next
            tmp_second = second.next

            first.next = second
            second.next = tmp_first

            second = tmp_second
            first = tmp_first

