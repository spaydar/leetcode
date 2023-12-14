"""
LeetCode #143. Reorder List

Reorder a singly-linked list of `n` nodes as follows:
    `1 > n > 2 > n-1 > 3 > n-2 > ...`
"""
from typing import Optional

class ListNode:
    """
    Definition for singly-linked list.
    """
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __eq__(self, __value: object) -> bool:
        if isinstance(__value, ListNode):
            r1, r2 = self, __value
            while r1 and r2:
                if r1.val != r2.val:
                    return False
                r1 = r1.next
                r2 = r2.next
            return r1 == None and r2 == None
        return False

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
    Unit tests for LeetCode 143. Reorder List
    """

    @staticmethod
    def create_n_list_nodes(n: int) -> Optional[ListNode]:
        """
        Create a linked list whose values increase from 1 to `n`
        """
        dummy = ListNode()
        runner = dummy
        i = 1
        while i <= n:
            runner.next = ListNode(i)
            runner = runner.next
            i += 1
        return dummy.next

    @staticmethod
    def create_n_list_nodes_reordered(n: int) -> Optional[ListNode]:
        """
        Creates a linked list containing `n` nodes reordered as defined in the problem
        """
        dummy = ListNode()
        runner = dummy
        l, r = 1, n
        while l <= r:
            runner.next = ListNode(l)
            runner = runner.next
            l += 1
            if l <= r:
                runner.next = ListNode(r)
                runner = runner.next
                r -= 1
        return dummy.next

    def test_0_nodes(self):
        l = self.create_n_list_nodes(0)
        reorder_list_linear_memory(l)
        self.assertEqual(l, self.create_n_list_nodes_reordered(0))

    def test_1_nodes(self):
        l = self.create_n_list_nodes(1)
        reorder_list_linear_memory(l)
        self.assertEqual(l, self.create_n_list_nodes_reordered(1))

    def test_4_nodes(self):
        l = self.create_n_list_nodes(4)
        reorder_list_linear_memory(l)
        self.assertEqual(l, self.create_n_list_nodes_reordered(4))

    def test_5_nodes(self):
        l = self.create_n_list_nodes(5)
        reorder_list_linear_memory(l)
        self.assertEqual(l, self.create_n_list_nodes_reordered(5))

    def test_extra_node(self):
        l = self.create_n_list_nodes(4)
        reorder_list_linear_memory(l)
        r = ListNode(0, self.create_n_list_nodes_reordered(4))
        self.assertNotEqual(l, r)

    def test_not_reordered(self):
        l = self.create_n_list_nodes(4)
        reorder_list_linear_memory(l)
        self.assertNotEqual(l, self.create_n_list_nodes(4))

if __name__ == '__main__':
    unittest.main()

