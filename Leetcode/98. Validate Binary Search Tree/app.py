# Definition for a binary tree node.
from ast import NodeVisitor, Num
from tkinter.tix import Tree
from typing import Optional

"""
# https://leetcode.com/problems/validate-binary-search-tree/
Description:
Input: root of Binary tree
Output: boolean 

Conditions for valid tree: 
1. The left subtree has nodes less than the current node
    Means that the current nodes left subtree has nodes and 
    those nodes all have to be less than the current node
2. The right subtree has nodes less than the current node
3. Both the left and right subtrees must also be binary trees 
    Both the subtrees must follow rule 1 and rule 2
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    @staticmethod
    def add_to_treeNode(tree_node: TreeNode, node: Num) -> TreeNode:
        return tree_node

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        """
        - use recursion to search the left and right subtrees
        """
        print(root.val)
        # check if left node is less than current node

        if root.left:
            if root.left.val < root.val:

                # continue checking the subtree
                if (self.isValidBST(root.left)) == False:
                    return False
            else:
                return False

        # check if right node is larger than current node
        if root.right:
            if root.right.val > root.val:
                # continue checking the subtree
                if (self.isValidBST(root.right)) == False:
                    return False
            else:
                return False
        return True


if __name__ == "__main__":

    # nodes = [2, 1, 3]
    # tree = TreeNode(2, TreeNode(1, None, None), TreeNode(3, None, None))
    # assert (Solution().isValidBST(tree)) == True

    # # nodes = [5, 1, 4, None, None, 3, 6]
    # tree = TreeNode(5, TreeNode(1, None, None), TreeNode(4, 3, 6))
    # print("hi", Solution().isValidBST(tree))
    # assert (Solution().isValidBST(tree)) == False

    # Add to the tree node ++++++++++++++++++EXTRA
    # nodes = [5, 4, 6, null, null, 3, 7]
    tree = TreeNode(5, TreeNode(4, None, None), TreeNode(6, TreeNode(3), TreeNode(7)))

    assert (Solution().isValidBST(tree)) == False


"""
# Answer 
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def traverse(node):
            if node == None:
                return True
            traverse(node.left)
            inorder.append(node.val)
            traverse(node.right)
        
        inorder = []
        traverse(root)
        for i in range(1, len(inorder)):
            if inorder[i] <= inorder[i - 1]:
                return False
        return True
"""
