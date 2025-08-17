class Node:
    def __init__(self):
        self.children = defaultdict(Node)
        self.end = False

class Trie:

    def __init__(self):
        self.root = Node()
        
    def insert(self, word: str) -> None:
        node = self.root
        for character in word:
            node = node.children[character]
        node.end = True

    def search(self, word: str) -> bool:
        node = self._walk(word)
        return node is not None and node.end

    def startsWith(self, prefix: str) -> bool:
        node = self._walk(prefix)
        return node is not None

    def _walk(self, word: str) -> Optional[Node]:
        node = self.root
        for character in word:
            node = node.children.get(character)
            if node is None:
                return None
        return node
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
