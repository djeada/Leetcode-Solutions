# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        '''
        if p is None and q is None:
            return True
        
        if p is None or q is None or p.val != q.val:
            return False

        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        '''

        queue = deque([(p, q)])

        while queue:

            node_a, node_b = queue.popleft()

            if node_a is None and node_b is None:
                continue
        
            if node_a is None or node_b is None or node_a.val != node_b.val:
                return False

            queue.append((node_a.left, node_b.left))    
            queue.append((node_a.right, node_b.right))

        return True  
