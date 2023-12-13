from typing import Optional

class ListNode:
    """
    Definition for singly-linked list.
    """
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self) -> str:
        return f'ListNode({self.val}) -> {self.next}'

def reorder_list(head: Optional[ListNode]) -> None:
    """
    Do not return anything, modify head in-place instead.
    """

def reorder_list_linear_memory(head: Optional[ListNode]) -> None:
    """
    Do not return anything, modify head in-place instead.
    """
    lst = list()
    runner = head
    while runner:
        tmp = runner.next
        runner.next = None
        lst.append(runner)
        runner = tmp
    print('lst', lst)
    runner = ListNode()
    while len(lst) > 0:
        runner.next = lst.pop(0)
        runner = runner.next
        if len(lst) > 0:
            runner.next = lst.pop()
            runner = runner.next

import unittest

class TestReorderList(unittest.TestCase):
    """
    docs TODO
    """

    @staticmethod
    def create_n_list_nodes(n: int) -> Optional[ListNode]:
        dummy = ListNode()
        runner = dummy
        i = 1
        while i <= n:
            runner.next = ListNode(i)
            runner = runner.next
            i += 1
        return dummy.next

    def test_reorder_list_linear_memory(self):
        l = self.create_n_list_nodes(4)
        print('ListNode before', l)
        self.assertIsNone(reorder_list_linear_memory(l))
        print('ListNode after', l)

if __name__ == '__main__':
    unittest.main()

