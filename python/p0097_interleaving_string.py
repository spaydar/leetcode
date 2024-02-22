def is_interleave_memo(s1: str, s2: str, s3: str) -> bool:
    if len(s1) + len(s2) != len(s3):
        return False
    memo = {}
    def dfs(i, j) -> bool:
        if i == len(s1) and j == len(s2):
            return True
        if (i, j) not in memo:
            if i < len(s1) and s1[i] == s3[i + j] and dfs(i + 1, j):
                return True
            elif j < len(s2) and s2[j] == s3[i + j] and dfs(i, j + 1):
                return True
            memo[(i, j)] = False
        return memo[(i, j)]
    return dfs(0, 0)

def is_interleave_table_2d(s1: str, s2: str, s3: str) -> bool:
    # TODO
    return False
