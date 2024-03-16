from leetcode_utils import ListNode
from typing import Optional

def reverse_k_group(head: Optional[ListNode], k: int) -> Optional[ListNode]:
    def reverse_segment(prev: Optional[ListNode], first: Optional[ListNode], last: Optional[ListNode]) -> Optional[ListNode]:
        while first is not last:
            next = first.next
            first.next = prev
            prev = first
            first = next
        return prev
    dummy = prev_group = ListNode(0, head)
    next_group = head
    while next_group:
        count = 0
        while count < k:
            if not next_group:
                return dummy.next
            next_group = next_group.next
            count += 1
        prev_group.next = reverse_segment(next_group, head, next_group)
        head.next = next_group
        prev_group = head
        head = next_group
    return dummy.next
