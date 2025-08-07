## Data Structures

* **`left, right`** - Two pointers for sliding window or binary search
* **`root`** - Root node of a binary tree

## Overall Approach

The problem asks us to check if one tree is subtree of another.

This solution uses the **Two Pointers** technique to efficiently traverse the data.

The algorithm works by:

1. **Step 1**
   
   ```python
   # Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
   ```
2. **Step 2**
   
   ```python
   def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        def isSame(node, subNode):
   ```

## Complexity Analysis

* **Time Complexity**: O(n)
* **Space Complexity**: O(h) where h is the height of the tree

## Key Insights

* Two pointers technique reduces time complexity from O(n²) to O(n)

## Source Code Analysis

```python
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
```

## Related Problems

* Similar problems involving the same algorithmic techniques
* Problems with related data structures or approaches
