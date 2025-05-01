# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # Build a map from node value to its index in inorder traversal.
        idx_map = {val: i for i, val in enumerate(inorder)}
        
        # Pointer into preorder list
        self.pre_idx = 0
        
        def helper(left: int, right: int) -> Optional[TreeNode]:
            # If there are no elements to construct the subtree
            if left > right:
                return None
            
            # Root value is next in preorder
            root_val = preorder[self.pre_idx]
            root = TreeNode(root_val)
            
            # Advance preorder index
            self.pre_idx += 1
            
            # Build left subtree
            root.left = helper(left, idx_map[root_val] - 1)
            # Build right subtree
            root.right = helper(idx_map[root_val] + 1, right)
            
            return root
        
        # Construct the tree spanning the full inorder range
        return helper(0, len(inorder) - 1)
