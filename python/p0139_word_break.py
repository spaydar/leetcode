from typing import List

def word_break_memo(s: str, word_dict: List[str]) -> bool:
    memo = {}
    def dfs(i: int) -> bool:
        if i == len(s):
            return True
        if i not in memo:
            for word in word_dict:
                if s[i:].startswith(word):
                    result = dfs(i + len(word))
                    if result:
                        memo[i] = (True, len(word))
                        break
            if i not in memo:
                memo[i] = (False, -1)
        return memo[i][0]
    return dfs(0)

def word_break_table(s: str, word_dict: List[str]) -> bool:
    table = [False for _ in range(len(s) + 1)]
    table[-1] = True
    for i in range(len(s) - 1, -1, -1):
        for word in word_dict:
            if s[i:].startswith(word) and table[i + len(word)]:
                table[i] = True
                break
    return table[0]
