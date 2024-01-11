from typing import List

def partition(s: str) -> List[List[str]]:
    result = []
    curr = []
    def is_palindrome(i: int, j: int) -> bool:
        while i < j:
            if s[i] != s[j]:
                return False
            i, j = i + 1, j - 1
        return True
    def dfs(i: int):
        if i == len(s):
            result.append(curr[:])
            return
        for j in range(i, len(s)):
            if is_palindrome(i, j):
                curr.append(s[i:j + 1])
                dfs(j + 1)
                curr.pop()
    dfs(0)
    return result

def partition_memo(s: str) -> List[List[str]]:
    result = []
    curr = []
    memo = {}
    def is_palindrome(i: int, j: int) -> bool:
        if (i, j) in memo:
            return memo[(i, j)]
        a, b = i, j
        while i < j:
            if s[i] != s[j]:
                memo[(a, b)] = False
                return False
            i, j = i + 1, j - 1
        memo[(a, b)] = True
        return True
    def dfs(i: int):
        if i == len(s):
            result.append(curr[:])
            return
        for j in range(i, len(s)):
            if is_palindrome(i, j):
                curr.append(s[i:j + 1])
                dfs(j + 1)
                curr.pop()
    dfs(0)
    return result
