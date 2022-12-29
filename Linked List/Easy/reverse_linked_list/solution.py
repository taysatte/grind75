
from typing import Optional

class ListNode:
    def __init__(self, val = 0, next = None) -> None:
        self.val = val
        self.next = next

class Solution:
    def reverse_list(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, current = None, head

        while current:
            next = current.next
            current.next = prev
            prev = current
            current = next
        
        return prev

    def reverse_list_recursive(self, head):
        def reverse(current, prev):
            if current is None:
                return prev
            else:
                next = current.next
                current.next = prev
                return reverse(next, current)

        return reverse(head, None)