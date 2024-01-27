from typing import List

def rob_memo(nums: List[int]) -> int:
    memo = {}
    def dfs(i: int) -> int:
        if i == len(nums) - 2:
            return max(nums[i], nums[i + 1])
        if i == len(nums) - 1:
            return nums[i]
        if i not in memo:
            memo[i] = max(nums[i] + dfs(i + 2), dfs(i + 1))
        return memo[i]
    return dfs(0)

def rob_table(nums: List[int]) -> int:
    if len(nums) == 1:
        return nums[0]
    table = nums[:]
    table[1] = max(table[0], table[1])
    for i in range(2, len(nums)):
        table[i] = table[i] + table[i - 2]
        table[i] = max(table[i], table[i - 1])
    return table[-1]

def rob_constant(nums: List[int]) -> int:
    sum_1, sum_2 = 0, 0
    for n in nums:
        next = max(sum_1 + n, sum_2)
        sum_1 = sum_2
        sum_2 = next
    return sum_2
