# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        def isSame(node, subNode):
            if not node and not subNode:
                return True
            if not node or not subNode:
                return False 
            if node.val != subNode.val:
                return False
            return (
                isSame(node.left, subNode.left)
                and isSame(node.right, subNode.right)
            )

        if root is None:
            return False

        if isSame(root, subRoot):
            return True

        return (
            self.isSubtree(root.left, subRoot)
            or self.isSubtree(root.right, subRoot)
        )
