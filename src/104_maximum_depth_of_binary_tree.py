# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        '''
        return max(1 + self.maxDepth(root.left), 1 + self.maxDepth(root.right))
        '''
        if not root:
            return 0

        queue = deque([root])
        depth = 0

        while queue:
            level_length = len(queue)
            for _ in range(level_length):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            depth += 1
        
        return depth
