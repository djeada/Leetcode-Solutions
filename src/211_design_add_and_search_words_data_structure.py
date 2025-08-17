from collections import defaultdict

class Node:
    def __init__(self):
        self.children = defaultdict(Node)
        self.end = False

class WordDictionary:

    def __init__(self):
        self.root = Node()

    def addWord(self, word: str) -> None:
        node = self.root
        for character in word:
            node = node.children[character]
        node.end = True

    def search(self, word: str) -> bool:
        def dfs(index, node):
            if index == len(word):
                return node.end

            character = word[index]
            if character == '.':
                for child in node.children.values():
                    if dfs(index + 1, child):
                        return True
                return False

            child = node.children.get(character)
            return dfs(index + 1, child) if child is not None else False

        return dfs(0, self.root)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
