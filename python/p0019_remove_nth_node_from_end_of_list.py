from leetcode_utils import ListNode
from typing import Optional

def remove_nth_from_end(head: Optional[ListNode], n: int) -> Optional[ListNode]:
    runner = head
    count = 0
    while runner:
        count += 1
        runner = runner.next
    runner = head
    i = 1
    while i < count - n:
        i += 1
        runner = runner.next
    if runner.next:
        runner.next = runner.next.next
    else:
        runner = None
    return head

def remove_nth_from_end_1_pass(head: Optional[ListNode], n: int) -> Optional[ListNode]:
    # TODO
    pass

def remove_nth_from_end_recursive(head: Optional[ListNode], n: int) -> Optional[ListNode]:
    # TODO
    pass

import unittest

class TestRemoveNthFromEnd(unittest.TestCase):
    """
    Unit tests for LeetCode 19. Remove Nth Node From End of List
    """

    @staticmethod
    def create_list_nodes_nth_from_end_removed(count: int, n: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        runner = dummy
        i = 1
        while i <= count:
            if i == count - n + 1:
                i += 1
            if runner:
                runner.next = ListNode(i)
                runner = runner.next
            i += 1
        return dummy.next

    removed_1st_from_1 = create_list_nodes_nth_from_end_removed(1, 1)
    removed_1st_from_4 = create_list_nodes_nth_from_end_removed(4, 1)
    removed_2nd_from_5 = create_list_nodes_nth_from_end_removed(5, 2)

    def test_1_nodes_1st_removed_from_end(self):
        self.assertEqual(remove_nth_from_end(ListNode.create_n_list_nodes(1), 1), self.removed_1st_from_1)

    def test_4_nodes_1st_removed_from_end(self):
        self.assertEqual(remove_nth_from_end(ListNode.create_n_list_nodes(4), 1), self.removed_1st_from_4)

    def test_5_nodes_2nd_removed_from_end(self):
        self.assertEqual(remove_nth_from_end(ListNode.create_n_list_nodes(5), 2), self.removed_2nd_from_5)

if __name__ == '__main__':
    unittest.main()

