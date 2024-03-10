from typing import List

def find_duplicate(nums: List[int]) -> int:
    slow = fast = 0
    while True:
        slow = nums[slow]
        fast = nums[nums[fast]]
        if slow == fast:
            break
    head = 0
    while head != slow:
        head = nums[head]
        slow = nums[slow]
    return head
