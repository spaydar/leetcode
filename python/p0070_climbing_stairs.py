def climb_stairs_memo(n: int) -> int:
    memo = {}
    def dfs(i: int) -> int:
        if i in memo:
            return memo[i]
        if i == 0:
            return 1
        if i == -1:
            return 0
        memo[i - 1] = dfs(i - 1)
        memo[i - 2] = dfs(i - 2)
        return memo[i - 1] + memo[i - 2]
    return dfs(n)

def climb_stairs_table(n: int) -> int:
    if n == 1:
        return 1
    table = [1 for _ in range(n)]
    table[1] = 2
    for i in range(2, n):
        table[i] = table[i - 1] + table[i - 2]
    return table[-1]

def climb_stairs_constant(n: int) -> int:
    one, two = 1, 1
    while n > 1:
        next = one + two
        one = two
        two = next
        n -= 1
    return two
