from leetcode_utils import ListNode
from typing import Optional

def reverse_k_group(head: Optional[ListNode], k: int) -> Optional[ListNode]:
    # TODO this doesn't work yet
    def reverse_segment(prev: Optional[ListNode], first: Optional[ListNode], last: Optional[ListNode]) -> Optional[ListNode]:
        while first is not last.next:
            next = first.next
            first.next = prev
            prev = first
            first = next
        return last
    dummy = slow = fast = ListNode(0, head)
    count = 0
    while fast:
        while count < k:
            if not fast:
                return dummy.next
            fast = fast.next
            count += 1
        count = 0
        # TODO reverse segment
