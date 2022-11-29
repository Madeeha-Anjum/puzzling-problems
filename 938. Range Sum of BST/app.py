"""
Solution:
    Trick: BST are recursed in order
    https://leetcode.com/problems/range-sum-of-bst/discuss/192579/Python-solution
"""
# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:

        # current node > target == go to left
        # current node < target == go to right
        # other we have the target

        curr_root = root
        # is the smaller tree found
        flag = False

        while not flag:
            if low <= curr_root.val <= high:
                flag = True

            if curr_root.val > low:
                curr_root = curr_root.left
            elif curr_root.val < low:
                curr_root = curr_root.right
            else:
                print("Done")

        return 4


def tree_node_as_string(root: TreeNode):

    if root is None:
        return ""

    string = f"TreeNode({root.val}, {tree_node_as_string(root.left)}, {tree_node_as_string(root.right)})"

    return string


def in_order(root: TreeNode):

    if root is None:
        return

    in_order(root.left)
    print(root.val)
    in_order(root.right)


def main():

    root = TreeNode(
        10, TreeNode(5, TreeNode(3), TreeNode(7)), TreeNode(15, None, TreeNode(18))
    )

    in_order(root)

    # print(tree_node_as_string(root))

    # s = Solution()
    # print(s.rangeSumBST(root, 3, 5))


if __name__ == "__main__":
    main()
