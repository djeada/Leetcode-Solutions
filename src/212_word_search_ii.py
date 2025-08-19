from collections import defaultdict

class Node:
    def __init__(self):
        self.children = defaultdict(Node)
        self.word = None

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        result = list()
        if not board or not board[0] or not words:
            return result

        m, n = len(board), len(board[0])

        # let's build the Trie
        self.root = Node()
        for word in words:
            node = self.root

            for character in word:
                node = node.children[character]
            node.word = word

        def dfs(i, j, node):
            if i < 0 or i >= m or j < 0 or j >= n:
                return

            character = board[i][j]
            if character == '#':
                return 

            child = node.children.get(character)
            if child is None:
                return
            if child.word:
                result.append(child.word)
                child.word = None
            
            board[i][j] = '#'

            dfs(i + 1, j, child)
            dfs(i - 1, j, child)
            dfs(i, j + 1, child)
            dfs(i, j - 1, child)

            board[i][j] = character

            if child.word is None and not child.children:
                del node.children[character]

        for i in range(m):
            for j in range(n):
                dfs(i, j, self.root)

        return result
