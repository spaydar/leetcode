from leetcode_utils import ListNode
from typing import Optional

def reverse_list_iterative(head: Optional[ListNode]) -> Optional[ListNode]:
    prev = None
    curr = head
    while curr:
        next = curr.next
        curr.next = prev
        prev = curr
        curr = next
    return prev

def reverse_list_recursive(head: Optional[ListNode]) -> Optional[ListNode]:
    if not head or not head.next:
        return head
    next = reverse_list_recursive(head.next)
    head.next.next = head
    head.next = None
    return next

def reverse_list_recursive_helper(head: Optional[ListNode]) -> Optional[ListNode]:
    def reverse(curr: Optional[ListNode], prev: Optional[ListNode]) -> Optional[ListNode]:
        if not curr:
            return prev
        next = curr.next
        curr.next = prev
        return reverse(next, curr)
    return reverse(head, None)
