from typing import List

def can_partition_memo(nums: List[int]) -> bool:
    # Exceeds Time Limit on LeetCode for large input: len(nums) == 198
    total = sum(nums)
    if total % 2 != 0:
        return False
    memo = {}
    def dfs(i: int, target: int) -> bool:
        curr = target - nums[i]
        if curr == 0:
            return True
        if curr < 0:
            return False
        if (i, target) not in memo:
            memo[(i, target)] = False
            for j in range(i + 1, len(nums)):
                if dfs(j, curr):
                    memo[(i, target)] = True
                    break
        return memo[(i, target)]
    for i in range(len(nums)):
        if dfs(i, total // 2):
            return True
    return False

def can_partition_table(nums: List[int]) -> bool:
    # TODO
    return False

def can_partition_set(nums: List[int]) -> bool:
    total = sum(nums)
    if total % 2 != 0:
        return False
    target = total // 2
    sums = set()
    for n in nums:
        if n == target:
            return True
        new_sums = set()
        for e in sums:
            if n + e == target:
                return True
            new_sums.add(n + e)
        sums = sums.union(new_sums)
        sums.add(n)
    return False
