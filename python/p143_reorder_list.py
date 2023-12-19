"""
LeetCode #143. Reorder List

Reorder a singly-linked list of `n` nodes as follows:
    `1 > n > 2 > n-1 > 3 > n-2 > ...`

The number of nodes in the list is in the range `[1, 5 * 10^4]`
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
        """
        Returns whether the value of each node in the given list equals that in self
        """
        if isinstance(__value, ListNode):
            r1, r2 = self, __value
            while r1 and r2:
                if r1.val != r2.val:
                    return False
                r1 = r1.next
                r2 = r2.next
            return r1 is None and r2 is None
        return False

    def __repr__(self) -> str:
        return f'ListNode({self.val}) -> {self.next}'

def reorder_list_constant_memory(head: Optional[ListNode]) -> None:
    """
    Reorders a linked list using constant memory, modifying the head in-place
    """
    if head is None or head.next is None:
        return
    # Find mid point of list
    slow, fast = head, head.next
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    # Separate first half from second
    second = slow.next
    prev = slow.next = None
    # Reverse second half of list
    while second:
        tmp = second.next
        second.next = prev
        prev = second
        second = tmp
    # Interleave lists
    left, right = head, prev
    while left and right:
        tmp_l = left.next
        tmp_r = right.next
        left.next = right
        right.next = tmp_l
        left = tmp_l
        right = tmp_r

def reorder_list_linear_memory(head: Optional[ListNode]) -> None:
    """
    Reorders a linked list using linear memory, modifying the head in-place
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

    reordered_0_nodes = create_n_list_nodes_reordered(0)
    reordered_1_nodes = create_n_list_nodes_reordered(1)
    reordered_4_nodes = create_n_list_nodes_reordered(4)
    reordered_5_nodes = create_n_list_nodes_reordered(5)
    reordered_50k_nodes = create_n_list_nodes_reordered(50000)
    reordered_4_plus_extra = ListNode(0, create_n_list_nodes_reordered(4))
    not_reordered_4_nodes = create_n_list_nodes(4)

    def test_0_nodes_constant_memory(self):
        l = self.create_n_list_nodes(0)
        reorder_list_constant_memory(l)
        self.assertEqual(l, self.reordered_0_nodes)

    def test_0_nodes_linear_memory(self):
        l = self.create_n_list_nodes(0)
        reorder_list_linear_memory(l)
        self.assertEqual(l, self.reordered_0_nodes)

    def test_1_nodes_constant_memory(self):
        l = self.create_n_list_nodes(1)
        reorder_list_constant_memory(l)
        self.assertEqual(l, self.reordered_1_nodes)

    def test_1_nodes_linear_memory(self):
        l = self.create_n_list_nodes(1)
        reorder_list_linear_memory(l)
        self.assertEqual(l, self.reordered_1_nodes)

    def test_4_nodes_constant_memory(self):
        l = self.create_n_list_nodes(4)
        reorder_list_constant_memory(l)
        self.assertEqual(l, self.reordered_4_nodes)

    def test_4_nodes_linear_memory(self):
        l = self.create_n_list_nodes(4)
        reorder_list_linear_memory(l)
        self.assertEqual(l, self.reordered_4_nodes)

    def test_5_nodes_constant_memory(self):
        l = self.create_n_list_nodes(5)
        reorder_list_constant_memory(l)
        self.assertEqual(l, self.reordered_5_nodes)

    def test_5_nodes_linear_memory(self):
        l = self.create_n_list_nodes(5)
        reorder_list_linear_memory(l)
        self.assertEqual(l, self.reordered_5_nodes)

    def test_50k_nodes_constant_memory(self):
        l = self.create_n_list_nodes(50000)
        reorder_list_constant_memory(l)
        self.assertEqual(l, self.reordered_50k_nodes)

    def test_50k_nodes_linear_memory(self):
        l = self.create_n_list_nodes(50000)
        reorder_list_linear_memory(l)
        self.assertEqual(l, self.reordered_50k_nodes)

    def test_extra_node_constant_memory(self):
        l = self.create_n_list_nodes(4)
        reorder_list_constant_memory(l)
        self.assertNotEqual(l, self.reordered_4_plus_extra)

    def test_extra_node_linear_memory(self):
        l = self.create_n_list_nodes(4)
        reorder_list_linear_memory(l)
        self.assertNotEqual(l, self.reordered_4_plus_extra)

    def test_not_reordered_constant_memory(self):
        l = self.create_n_list_nodes(4)
        reorder_list_constant_memory(l)
        self.assertNotEqual(l, self.not_reordered_4_nodes)

    def test_not_reordered_linear_memory(self):
        l = self.create_n_list_nodes(4)
        reorder_list_linear_memory(l)
        self.assertNotEqual(l, self.not_reordered_4_nodes)

if __name__ == '__main__':
    unittest.main()

