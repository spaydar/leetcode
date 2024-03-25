from typing import List

def three_sum(nums: List[int]) -> List[List[int]]:
    result = []
    nums.sort()
    i = 0
    while i < len(nums) - 2:
        j, k = i + 1, len(nums) - 1
        while j < k:
            val = nums[i] + nums[j] + nums[k]
            if val < 0:
                j += 1
            elif val > 0:
                k -= 1
            else:
                result.append([nums[i], nums[j], nums[k]])
                j += 1
                while j < k and nums[j] == nums[j - 1]:
                    j += 1
        i += 1
        while i < len(nums) and nums[i] == nums[i - 1]:
            i += 1
    return result

def three_sum_always_skip_repeated_nums(nums: List[int]) -> List[List[int]]:
    result = []
    nums.sort()
    i = 0
    while i < len(nums) - 2:
        j, k = i + 1, len(nums) - 1
        while j < k:
            val = nums[i] + nums[j] + nums[k]
            if val == 0:
                result.append([nums[i], nums[j], nums[k]])
                val -= 1
            if val < 0:
                j += 1
                while j < k and nums[j] == nums[j - 1]:
                    j += 1
            elif val > 0:
                k -= 1
        i += 1
        while i < len(nums) and nums[i] == nums[i - 1]:
            i += 1
    return result
