# Merge Two Sorted Lists

```
Author: Taylor Sattenfield
Date: 12 December 2022
```

## Problem

You are given the heads of two sorted linked lists ```list1``` and ```list2```.

Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return <i>the head of the merged linked list.</i>

<center><a href="https://ibb.co/pnrpZwD"><img src="https://i.ibb.co/vDv8mq5/merge-ex.png" alt="merge-ex" border="0"></a></center>

### Example 1:

```
Input: list1 = [1, 2, 4], list2 = [1, 3, 4]
Output: [1, 1, 2, 3, 4, 4]
```

### Example 2:

```
Input: list1 = [], list2 = []
Output: []
```

### Example 3:

```
Input: list1 = [], list2 = [0]
Output: [0]
```

Constraints:<br>

```The number of nodes in both lists is in the range [0, 50]```<br><br>
```-100 <= node.val <= 100```<br><br>
```Both list1 and list2 are sorted in non-decreasing order```<br><br>

# Explanation

This problem requires some basica fundamental knowledge of how linked list nodes are constructed and how linked lists work in general. The approach is pretty straight-forward:
<ul>
  <li>Create a dummy head node to create a new sorted linked list
   <li>Start with a pointer at the head of each list
    <li>Walk down each list comparing the data within the nodes of each list
    <li>If the data from list1 is less than <i>list2</i> append it to the new list; else, append <i>list2's</i> data to the list
</ul>
There's a couple edge cases that need to be handled, such as the case for when the lists are not equal in length. Since the lists are already in sorted order, once one list has been exhausted, the longer list can just get appended to the back of the new list.
<br><br>

``` python3
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        head = dummy

        while list1 and list2:
            if list1.val < list2.val:
                head.next = list1
                list1 = list1.next
            else:
                head.next = list2
                list2 = list2.next
            head = head.next
        
        if list1:
            head.next = list1
            list1 = list1.next
        if list2:
            head.next = list2
            list2 = list2.next

        return dummy.next
```
