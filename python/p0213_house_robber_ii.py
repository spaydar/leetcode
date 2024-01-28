from typing import List

def rob_memo(nums: List[int]) -> int:
    if len(nums) == 1:
        return nums[0]
    def helper(start: int, end: int):
        memo = {}
        def dfs(i: int) -> int:
            if i == end:
                return 0
            if i == end - 1:
                return nums[i]
            if i not in memo:
                memo[i] = max(nums[i] + dfs(i + 2), dfs(i + 1))
            return memo[i]
        return dfs(start)
    return max(helper(0, len(nums) - 1), helper(1, len(nums)))

def rob_table(nums: List[int]) -> int:
    if len(nums) == 1:
        return nums[0]
    if len(nums) == 2:
        return max(nums[0], nums[1])
    def helper(start: int, end: int):
        table = nums[start:end]
        table[1] = max(table[0], table[1])
        for i in range(2, len(table)):
            table[i] = table[i] + table[i - 2]
            table[i] = max(table[i], table[i - 1])
        return table[-1]
    return max(helper(0, len(nums) - 1), helper(1, len(nums)))

def rob_constant(nums: List[int]) -> int:
    if len(nums) == 1:
        return nums[0]
    def helper(start: int, end: int):
        one, two = 0, 0
        for n in nums[start:end]:
            next = max(n + one, two)
            one = two
            two = next
        return two
    return max(helper(0, len(nums) - 1), helper(1, len(nums)))
