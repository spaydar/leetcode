from leetcode_utils import ListNode
from typing import Optional

def reverse_k_group(head: Optional[ListNode], k: int) -> Optional[ListNode]:
    # TODO this doesn't work yet
    dummy = group_prev = fast = ListNode(0, head)
    count = 0
    while fast:
        while count < k:
            if not fast:
                return dummy.next
            fast = fast.next
            count += 1
        prev, group_next, runner = fast.next, fast.next, group_prev.next
        count = 0
        while runner is not group_next:
            next = runner.next
            runner.next = prev
            prev = runner
            runner = next
        tmp = group_prev.next
        group_prev.next = fast
        group_prev = tmp
