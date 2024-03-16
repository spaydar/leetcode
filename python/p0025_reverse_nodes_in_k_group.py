from leetcode_utils import ListNode
from typing import Optional

def reverse_k_group(head: Optional[ListNode], k: int) -> Optional[ListNode]:
    def reverse_segment(cur: Optional[ListNode], next_group: Optional[ListNode]) -> Optional[ListNode]:
        prev = next_group
        while cur is not next_group:
            next = cur.next
            cur.next = prev
            prev = cur
            cur = next
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
        prev_group.next = reverse_segment(head, next_group)
        head.next = next_group
        prev_group = head
        head = next_group
    return dummy.next
