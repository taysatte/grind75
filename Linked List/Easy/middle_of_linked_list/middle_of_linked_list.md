# Middle of the Linked List

```
Author: Taylor Sattenfield
Date: 28 December 2022
```

## Problem

Given the ```head``` of a singly linked list, return <i>the middle node of the linked list.</i>

If there are two middle nodes, return <b>the second middle</b> node.

### Example 1:

```
Input: head = [1,2,3,4,5]
Output: [3,4,5]
Explanation: The middle node of the list is node 3.
```
### Example 2:

```
Input: head = [1,2,3,4,5,6]
Output: [4,5,6]
Explanation: Since the list has two middle nodes with values 3 and 4, we return the second one.
```

Constraints:<br>

```The number of the nodes in the list is in the range [0, 100].```<br><br>
```1 <= Node.val <= 100```<br><br>

# Explanation

<ul>
<li>Use two pointers mid and end
<li>The mid pointer will iterate by one (next), while the end pointer iterates by two (next.next)
<li>When the end pointer reaches the end of the list (end.next == None), mid will be at the middle of the list
<li>Then we can return the middle node
</ul>

``` python3
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
```
