from typing import List

def permutations(nums: List[int]) -> List[List[int]]:
    result = []
    curr = []
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

# On LeetCode, not using a 'visited' set runs faster, perhaps because nums' length is relatively short i.e. <=6 elements
def permutations_with_set(nums: List[int]) -> List[List[int]]:
    result = []
    curr = []
    visited = set()
    def dfs():
        if len(curr) == len(nums):
            result.append(curr[:])
            return
        for i in nums:
            if i not in visited:
                visited.add(i)
                curr.append(i)
                dfs()
                curr.pop()
                visited.remove(i)
    dfs()
    return result
