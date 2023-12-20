from __future__ import annotations
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

class TreeNode:
    """
    Definition for a binary tree node.
    """
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
