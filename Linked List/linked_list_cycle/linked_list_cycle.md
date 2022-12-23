# Linked List Cycle

```
Author: Taylor Sattenfield
Date: 19 December 2022
```

## Problem

Given ```head```, the head of a linked list, determine if the linked list has a cycle in it.

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the ```next``` pointer. Internally, ```pos``` is used to denote the index of the node that tail's ```next``` pointer is connected to. Note that ```pos``` is not passed as a parameter.

Return ```true``` if there is a cycle in the linked list. Otherwise, return ```false```.

### Example 1:

```
Input: head = [3, 2, 0, -4], pos = 1
Output: True
Explanation: There is a cycle in the linked list, where the tail connects to the 1st node (0-indexed).
```
### Example 2:

```
Input: head = [1, 2], pos = 0
Output: True
Explanation: There is a cycle in the linked list, where the tail connects to the 0th node.
```

### Example 3:

```
Input: head = [1], pos = -1
Output: False
Explanation: There is no cycle in the linked list.
```

Constraints:<br>

```The number of the nodes in the list is in the range [0, 10^4].```<br><br>
```-10^5 <= Node.val <= 10^5```<br><br>
```pos is -1 or a valid index in the linked-list.```<br><br>

# Explanation

The goal of the problem is to find if a given linked list has a cycle in it. This problem introduced me to Floyd's tortoise and hare algorithm, which is implemented in the solution below. The algorithm uses two pointers, fast and slow, that if a cycle exists in the linked list, the pointers will eventually meet up at a certain position. If the pointers never meet each other, we return false, as there is no cycle present in the list.

``` python3
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
```
