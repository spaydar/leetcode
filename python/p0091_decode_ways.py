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

def num_decodings_table(s: str) -> int:
    table = [0 for _ in range(len(s) + 2)]
    table[1] = 1
    for i in range(0, len(s)):
        t = i + 2
        table[t] = 0 if s[i] == '0' else table[t - 1]
        if i > 0 and (s[i - 1] == '1' or (s[i - 1] == '2' and s[i] < '7')):
            table[t] += table[t - 2]
    return table[-1]

def num_decodings_constant(s: str) -> int:
    prev, curr = 0, 1
    i = 0
    while i < len(s):
        next = 0 if s[i] == '0' else curr
        if i > 0 and (s[i - 1] == '1' or (s[i - 1] == '2' and s[i] < '7')):
            next += prev
        prev, curr = curr, next
        i += 1
    return curr
