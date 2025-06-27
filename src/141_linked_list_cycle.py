# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # Option 1: keep track of nodes we've seen
        # visited = set()
        # node = head

        # while node:
        #    node = node.next
        #    if node in visited:
        #        return True
        #    visited.add(node)

        # return False

        # Option 2: use slow and fast pointers
        slow = fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True


        return False
