# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string."""
        vals = []
        def dfs(node):
            if node:
                vals.append(str(node.val))
                dfs(node.left)
                dfs(node.right)
            else:
                vals.append('#')    # null marker
        dfs(root)
        return ','.join(vals)

    def deserialize(self, data):
        """Decodes your encoded data to tree."""
        tokens = data.split(',')
        self.i = 0

        def dfs():
            if self.i >= len(tokens):
                return None
            tok = tokens[self.i]
            self.i += 1
            if tok == '#':
                return None
            node = TreeNode(int(tok))
            node.left  = dfs()
            node.right = dfs()
            return node

        return dfs()
