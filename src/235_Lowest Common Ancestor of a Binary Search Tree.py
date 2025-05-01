# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(
        self,
        root: 'TreeNode',
        p: 'TreeNode',
        q: 'TreeNode'
    ) -> 'TreeNode':
        # Ensure p.val <= q.val for simpler comparisons (optional)
        if p.val > q.val:
            p, q = q, p

        # --- Recursive approach ---
        def recurse(node: 'TreeNode') -> 'TreeNode':
            # both targets are smaller → go left
            if node.val > q.val:
                return recurse(node.left)
            # both targets are larger → go right
            if node.val < p.val:
                return recurse(node.right)
            # split point found
            return node

        # --- Iterative approach ---
        def iterate(node: 'TreeNode') -> 'TreeNode':
            while node:
                # go left
                if node.val > q.val:
                    node = node.left
                # go right
                elif node.val < p.val:
                    node = node.right
                # split point
                else:
                    return node
            return None  # just in case

        # Choose one:
        # return recurse(root)
        return iterate(root)
