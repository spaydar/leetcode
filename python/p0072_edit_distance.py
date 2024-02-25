def min_distance_memo(word1: str, word2: str) -> int:
    memo = {}
    def dfs(i: int, j: int) -> int:
        if i == len(word1) and j == len(word2):
            return 0
        if i == len(word1):
            return len(word2) - j
        if j == len(word2):
            return len(word1) - i
        if (i, j) not in memo:
            if word1[i] == word2[j]:
                memo[(i, j)] = dfs(i + 1, j + 1)
            else:
                replace = dfs(i + 1, j + 1)
                delete = dfs(i + 1, j)
                insert = dfs(i, j + 1)
                memo[(i, j)] = 1 + min(replace, delete, insert)
        return memo[(i, j)]
    return dfs(0, 0)

def min_distance_table_2d(word1: str, word2: str) -> int:
    dp = [[0 for _ in range(len(word2) + 1)] for _ in range(len(word1) + 1)]
    for i in range(len(word1) + 1):
        dp[i][-1] = len(word1) - i
    for j in range(len(word2) + 1):
        dp[-1][j] = len(word2) - j
    for i in range(len(word1) - 1, -1, -1):
        for j in range(len(word2) - 1, -1, -1):
            if word1[i] == word2[j]:
                dp[i][j] = dp[i + 1][j + 1]
            else:
                dp[i][j] = 1 + min(dp[i + 1][j + 1], dp[i + 1][j], dp[i][j + 1])
    return dp[0][0]

def min_distance_table_1d(word1: str, word2: str) -> int:
    prev = [i for i in range(len(word2), -1, -1)]
    curr = [1 for _ in range(len(word2) + 1)]
    for i in range(len(word1) - 1, -1, -1):
        for j in range(len(word2) - 1, -1, -1):
            if word1[i] == word2[j]:
                curr[j] = prev[j + 1]
            else:
                curr[j] = 1 + min(prev[j + 1], prev[j], curr[j + 1])
        for k in range(len(curr)):
            prev[k] = curr[k]
        curr[-1] += 1
    return prev[0]

def min_distance_queue(word1: str, word2: str) -> int:
    from collections import deque
    if not word1 or not word2:
        return max(len(word1), len(word2))
    queue, visited, result = deque(), set(), 0
    queue.append((0,0))
    while queue:
        for _ in range(len(queue)):
            i, j = queue.popleft()
            while i < len(word1) and j < len(word2) and word1[i] == word2[j]:
                i += 1
                j += 1
            if i == len(word1) and j == len(word2):
                return result
            for x, y in [(i + 1, j + 1), (i, j + 1), (i + 1, j)]:
                if x <= len(word1) and y <= len(word2) and (x, y) not in visited:
                    visited.add((x, y))
                    queue.append((x, y))
        result += 1
    return result
