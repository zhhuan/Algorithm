"""
-----------------------
File name   : validate_BST.py
Description : Given a binary tree, determine if it is a valid binary search tree (BST).
Author      : 钟寰
Time        : 2016-12-24 9:45
-----------------------
"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def isValidBST(self, root):
        """
        :param root: TreeNode
        :return: bool
        """
        self.prev = None
        self.isBST = True
        self.inorder_search(root)
        return self.isBST

    def inorder_search(self,node):
        """judge node is smaller than previous node or not.
        :param node:TreeNode
        :return:
        """
        if not node:
            return
        self.inorder_search(node.left)
        if self.prev and node.val <= self.prev.val:  # like [1,1] isn't BST
            self.isBST = False
        self.prev = node
        self.inorder_search(node.right)