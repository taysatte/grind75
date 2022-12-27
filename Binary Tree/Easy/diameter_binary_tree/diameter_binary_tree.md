# Invert Binary Tree

```
Author: Taylor Sattenfield
Date: 26 December 2022
```

## Problem

Given the ```root``` of a binary tree, return <i>the length of the <b>diameter</b> of the tree.</i>

The <b>diameter</b> of a binary tree is the <b>length</b> of the longest path between any two nodes in a tree. This path may or may not pass through the ```root```.

The <b>length</b> of a path between two nodes is represented by the number of edges between them.

### Example 1:

```
Input: root = [1,2,3,4,5]
Output: 3
Explanation: 3 is the length of the path [4,2,1,3] or [5,2,1,3].
```
### Example 2:

```
Input: root = [1,2]
Output: 1
```

Constraints:<br>

```The number of nodes in the tree is in the range [0, 10^4].```<br><br>
```-100 <= Node.val <= 100```<br><br>

# Explanation

<ul>
<li>
</ul>

``` python3
class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def diameter_of_binary_tree(self, root: Optional[TreeNode]) -> int:
        res = [0]

        def dfs(root):
            if not root:
                return -1
            left = dfs(root.left)
            right = dfs(root.right)
            res[0] = max(res[0], 2 + left + right)

            return 1 + max(left, right)
        
        dfs(root)
        return res[0]

```
