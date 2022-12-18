# Invert Binary Tree

```
Author: Taylor Sattenfield
Date: 15 December 2022
```

## Problem

Given the ```root``` of a binary tree, invert the tree, and return <i>its root</i>.

### Example 1:

```
Input: root = [2, 1, 3]
Output: [2, 3, 1]
```
### Example 2:

```
Input: root = []
Output: []
```

Constraints:<br>

```The number of nodes in the tree is in the range [0, 100].```<br><br>
```-100 <= Node.val <= 100```<br><br>

# Explanation

This problem is pretty simple once you can somewhat grasp the idea of recursion and how a tree is constructed. For a little background info: a binary tree is a data structure that is constructed by ```TreeNode```'s. At each node there exists a value and pointers to its child ```TreeNode```'s (left and right). Essentially, a tree is made up from a bunch of subtrees, which serves as a perfect candidate problem for a recursive algorithm.

Inverting a tree is basically traveresing the tree down both sides and swapping the children at each node on the way back up. 

So, here's the main idea:

<ul>
<li>Establish a base case (if the <i>root == null</i>, return <i>root</i>)
<li>Set up the swapping operation to swap the children nodes
<li>Recursively call the <i>invert_tree()</i> function on both sides of the tree
<li>Once the recursive operations reach the end, the main function will return <i>root</i>
</ul>

``` python3
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invert_tree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # Base Case
        if not root:
            return root

        # Swap the children
        temp = root.left
        root.left = root.right
        root.right = temp
        
        self.invert_tree(root.left)
        self.invert_tree(root.right)

        return root
```
