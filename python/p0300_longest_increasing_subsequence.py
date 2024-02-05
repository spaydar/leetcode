from typing import List

def length_of_lis_memo(nums: List[int]) -> int:
    # Exceeds Memory Limit on LeetCode for large input
    memo = {}
    def dfs(i: int, prev_i: int) -> int:
        if i == len(nums):
            return 0
        if (i, prev_i) not in memo:
            skip = dfs(i + 1, prev_i)
            take = -1
            if prev_i == -1 or nums[i] > nums[prev_i]:
                take = 1 + dfs(i + 1, i)
            memo[(i, prev_i)] = max(skip, take)
        return memo[(i, prev_i)]
    return dfs(0, -1)

def length_of_lis_table(nums: List[int]) -> int:
    table = [1 for _ in nums]
    for i in range(len(nums)):
        for j in range(0, i):
            if nums[j] < nums[i]:
                table[i] = max(table[i], 1 + table[j])
    return max(table)

def length_of_lis_binary(nums: List[int]) -> int:
    result = [nums[0]]
    for i in range(1, len(nums)):
        if nums[i] > result[-1]:
            result.append(nums[i])
        else:
            low, high = 0, len(result) - 1
            while low < high:
                mid = (low + high) // 2
                if result[mid] < nums[i]:
                    low = mid + 1
                else:
                    high = mid
            result[low] = nums[i]
    return len(result)
