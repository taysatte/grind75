
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        mid, end = head, head
        
        while end != None and end.next != None:
            mid = mid.next
            end = end.next.next

        return mid