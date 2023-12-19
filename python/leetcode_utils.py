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
