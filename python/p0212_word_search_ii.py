from typing import List, Set, Tuple

class Trie():
    # We don't define `search` fn as `find_words` fn will search the Trie
    def __init__(self) -> None:
        self.is_end = False
        self.children = {}

    def insert(self, word: str) -> None:
        curr = self
        for c in word:
            if c not in curr.children:
                curr.children[c] = Trie()
            curr = curr.children[c]
        curr.is_end = True

def find_words(board: List[List[str]], words: List[str]) -> List[str]:
    NUM_ROWS, NUM_COLS = len(board), len(board[0])
    result, trie = set(), Trie()
    for word in words:
        trie.insert(word)
    visited: Set[Tuple[int, int]] = set()
    chars: List[str] = []
    def dfs(i: int, j: int, node: Trie) -> bool:
        if (i < 0 or j < 0 or
            i == NUM_ROWS or j == NUM_COLS or
            (i, j) in visited or board[i][j] not in node.children
        ):
            return False
        visited.add((i, j))
        chars.append(board[i][j])
        node = node.children[board[i][j]]
        should_prune = False
        if node.is_end:
            word = ''.join(chars)
            if word not in result:
                result.add(word)
            if not node.children:
                should_prune = True
        for r, c in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
            if dfs(r, c, node):
                del node.children[board[r][c]]
                should_prune = True
        visited.remove((i, j))
        chars.pop()
        return should_prune and not node.children
    for i in range(NUM_ROWS):
        for j in range(NUM_COLS):
            dfs(i, j, trie)
    return list(result)

