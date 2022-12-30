# Maximum Depth of Binary Tree

```
Author: Taylor Sattenfield
Date: 29 December 2022
```

## Problem

Given the ```root``` of a binary tree, return <i>its maximum depth.</i>

A binary tree's <b>maximum depth</b> is the number of nodes along the longest path from the root node down to the farthest leaf node.

### Example 1:

```
Input: root = [3, 9, 20, null, null, 15, 7]
Output: 3
```
### Example 2:

```
Input: root = [1, null, 2]
Output: 2
```

Constraints:<br>

```The number of nodes in the tree is in the range [0, 10^4].```<br><br>
```-100 <= Node.val <= 100```<br><br>

# Explanation

<ul>
<li>Establish base case of if root == None, return 0
<li>Perform a DFS on both sides of the binary tree
<li>Return the tree's maximum depth (maximum number of nodes along the longest path)
</ul>

``` python3
class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def max_depth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        return 1 + max(self.max_depth(root.left), self.max_depth(root.right))
```
