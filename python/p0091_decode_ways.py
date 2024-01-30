def num_decodings_memo(s: str) -> int:
    memo = {}
    def dfs(i: int) -> int:
        if i >= len(s):
            return 1
        if s[i] == '0':
            return 0
        if (
            i + 1 < len(s) and
            (s[i] == '1' or (s[i] == '2' and -1 < int(s[i + 1]) < 7))
        ):
            if i not in memo:
                memo[i] = dfs(i + 1) + dfs(i + 2)
            return memo[i]
        if i not in memo:
            memo[i] = dfs(i + 1)
        return memo[i]
    return dfs(0)

def num_decodings_constant(s: str) -> int:
    # TODO
