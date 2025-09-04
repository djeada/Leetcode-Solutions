# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

import math
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.best = -math.inf

        def dfs(node):
            if not node:
                return 0

            left = max(dfs(node.left), 0)
            right = max(dfs(node.right), 0)

            self.best = max(self.best, node.val + left + right)
            return node.val + max(left, right)


        dfs(root)
        return self.best
            
