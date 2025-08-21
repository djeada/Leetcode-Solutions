# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        '''
        if root is None:
            return None

        root.left, root.right = self.invertTree( root.right ), self.invertTree( root.left )
        return root 
        '''
        if root is None:
            return None

        queue = deque([root])
        while queue:
            node = queue.pop()
            if node is None:
                continue
            node.left, node.right = node.right, node.left
            queue.append(node.left)
            queue.append(node.right)

        return root 

        
