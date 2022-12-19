
from typing import Optional

class ListNode:
    def __init__(self, val = 0):
        self.val = val
        self.next = None

class Solution:
    def has_cycle(self, head: Optional[ListNode]) -> bool:
        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False