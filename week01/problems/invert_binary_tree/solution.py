
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def invert_tree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # Base case
        if not root:
            return root

        # Swap the children
        temp = root.left
        root.left = root.right
        root.right = temp

        self.invert_tree(root.left)
        self.invert_tree(root.right)

        return root