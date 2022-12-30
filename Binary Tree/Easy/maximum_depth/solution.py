
from collections import deque
from typing import Optional

class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # Recursive DFS
    def max_depth_dfs_recur(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        return 1 + max(self.max_depth_dfs(root.left), self.max_depth_dfs(root.right))

    # BFS
    def max_depth_bfs(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        lvl = 0
        q = deque([root])

        while q:
            for i in range(len(q)):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            lvl += 1
        return lvl

    # Iterative DFS
    def max_depth_dfs_iter(self, root: Optional[TreeNode]) -> int:
        stack = [[root, 1]]
        res = 0

        while stack:
            node, depth = stack.pop()

            if node:
                res = max(res, depth)
                stack.append([node.left, depth + 1])
                stack.append([node.right, depth + 1])
        return res
                





