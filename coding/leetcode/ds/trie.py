
class TrieNode:
    def __init__(self):
        self.edge = {}
        self.end = False

    def put(self, char):
        if char in self.edge:
            return self.edge[char]
        self.edge[char] = TrieNode()
        return self.edge[char]

    def get(self, char):
        return self.edge[char] if char in self.edge else None


class Trie:

    def __init__(self):
        self._root = TrieNode()

    def _search(self, word: str) -> TrieNode:
        node = self._root
        for char in word:
            node = node.get(char)
            if node is None:
                break
        return node

    def insert(self, word: str) -> None:
        node = self._root
        for char in word:
            node = node.put(char)
        node.end = True

    def search(self, word: str) -> bool:
        node = self._search(word)
        return node is not None and node.end

    def startsWith(self, prefix: str) -> bool:
        node = self._search(prefix)
        return node is not None


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)