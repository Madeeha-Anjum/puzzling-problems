# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return f"TreeNode({self.val}, {self.left}, {self.right})"


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        """
        # Loop each tree at the same time and compare the val
        """
        if p is None and q is None:
            return True

        if (p is None) ^ (q is None):
            return False

        if p.val == q.val:
            return self.isSameTree(p.right, q.right) and self.isSameTree(p.left, q.left)

        return False


if __name__ == "__main__":
    root_p = TreeNode(1, TreeNode(2, None, None), TreeNode(3, None, None))
    root_q = TreeNode(1, TreeNode(2, None, None), TreeNode(3, None, None))

    assert Solution().isSameTree(root_p, root_q) is True

    root_x = TreeNode(1, TreeNode(2, None, None), None)
    root_y = TreeNode(1, None, TreeNode(2, None, None))

    assert Solution().isSameTree(root_x, root_y) is False
