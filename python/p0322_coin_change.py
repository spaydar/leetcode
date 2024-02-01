from typing import List

def coin_change_memo(coins: List[int], amount: int) -> int:
    memo = {}
    def dfs(remaining: int) -> int:
        if remaining == 0:
            return 0
        if remaining < 0:
            return -1
        if remaining not in memo:
            for c in coins:
                result = dfs(remaining - c)
                if result > -1 and (remaining not in memo or result < memo[remaining]):
                    memo[remaining] = 1 + result
            if remaining not in memo:
                memo[remaining] = -1
        return memo[remaining]
    return dfs(amount)

def coin_change_table_neg1(coins: List[int], amount: int) -> int:
    table = [-1 for _ in range(amount + 1)]
    table[0] = 0
    for i in range(1, amount + 1):
        for c in coins:
            remaining = i - c
            if (remaining > -1 and table[remaining] != -1 and
                (table[i] == -1 or 1 + table[remaining] < table[i])
            ):
                table[i] = 1 + table[remaining]
    return table[-1]

def coin_change_table_max(coins: List[int], amount: int) -> int:
    table = [amount + 1 for _ in range(amount + 1)]
    table[0] = 0
    for i in range(1, amount + 1):
        for c in coins:
            if i - c > -1:
                table[i] = min(table[i], 1 + table[i - c])
    return table[amount] if table[amount] != amount + 1 else -1

def coin_change_bit_ops(coins: List[int], amount: int) -> int:
    # TODO
    return -1
