from leetcode_utils import ListNode
from typing import Optional

def add_two_numbers(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    dummy = curr = ListNode(-1)
    carry = 0
    while l1 and l2:
        temp = l1.val + l2.val + carry
        carry = temp // 10
        curr.next = ListNode(temp % 10)
        curr = curr.next
        l1 = l1.next
        l2 = l2.next
    while l1:
        temp = l1.val + carry
        carry = temp // 10
        curr.next = ListNode(temp % 10)
        curr = curr.next
        l1 = l1.next
    while l2:
        temp = l2.val + carry
        carry = temp // 10
        curr.next = ListNode(temp % 10)
        curr = curr.next
        l2 = l2.next
    if carry:
        curr.next = ListNode(carry)
    return dummy.next

def add_two_numbers_recursive(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    def helper(l1: Optional[ListNode], l2: Optional[ListNode], carry: int) -> Optional[ListNode]:
        if not l1 and not l2 and not carry:
            return None
        left = l1.val if l1 else 0
        right = l2.val if l2 else 0
        temp = left + right + carry
        return ListNode(temp % 10, helper(l1.next if l1 else None, l2.next if l2 else None, temp // 10))
    return helper(l1, l2, 0)
