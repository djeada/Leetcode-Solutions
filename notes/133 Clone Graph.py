"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if node is None:
            return None

        # Map from original node.val to its clone
        cloned: Dict[int, Node] = {}

        def dfs(orig: 'Node') -> 'Node':
            # If we've already cloned this node, return it
            if orig.val in cloned:
                return cloned[orig.val]
            # Otherwise, create the clone and register it
            copy = Node(orig.val)
            cloned[orig.val] = copy
            # Recursively clone all neighbors
            for nbr in orig.neighbors:
                copy.neighbors.append(dfs(nbr))
            return copy

        return dfs(node)
