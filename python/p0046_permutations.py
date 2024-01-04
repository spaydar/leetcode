from typing import List

def permutations(nums: List[int]) -> List[List[int]]:
    result = []
    curr = []
    # On LeetCode, not using a 'visited' set runs faster, perhaps because nums' length is relatively short i.e. <=6 elements
    def dfs():
        if len(curr) == len(nums):
            result.append(curr[:])
            return
        for i in nums:
            if i not in curr:
                curr.append(i)
                dfs()
                curr.pop()
    dfs()
    return result
