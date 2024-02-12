class TrieNode():
    def __init__(self):
        self.is_end = False
        self.children = {}

class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def add_word(self, word: str) -> None:
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.is_end = True

    def search(self, word: str) -> bool:
        def dfs(curr: TrieNode, i: int) -> bool:
            if i == len(word):
                return curr.is_end
            if word[i] == '.':
                for child in curr.children.values():
                    if dfs(child, i + 1):
                        return True
                return False
            if word[i] in curr.children:
                return dfs(curr.children[word[i]], i + 1)
            return False
        return dfs(self.root, 0)
