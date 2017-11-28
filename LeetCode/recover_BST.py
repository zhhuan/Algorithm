"""
File name   : recover_BST.py
Description : Two elements of a binary search tree (BST) are swapped by mistake.
              Recover the tree without changing its structure.
Author      : 钟寰
Time        : 2016-12-23 17:21
"""


class TreeNode(object):
    """The TreeNode object define a binary tree node.
    Including value,left child node,right child node.
    """
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    # average O(lgn) space (worst case, O(n) space), recursively, one-pass
    def recoverTree(self, root):
        """Modify root in-place(swapped by mistake)
        :param root: TreeNode
        :returns void Do not return anything.
        """
        self.prev = None
        self.n1 = self.n2 = None
        self.inorder_tree_walk(root)
        self.n1.val , self.n2.val = self.n2.val, self.n1.val

    def inorder_tree_walk(self,node):
        """Inorder tree walk the root,find out two exchanged node.
        recursive results is arranged by numerical size.If one node's
        val < node.prev's val,it or its prev must have wrong position
        :param node:the root node
        :returns
        """
        if not node:
            return
        self.inorder_tree_walk(node.left)
        if  self.prev and node.val < self.prev.val:
            if not self.n1:
                self.n1 , self.n2 = self.prev, node
            else:
                self.n2 = node
        self.prev = node
        self.inorder_tree_walk(node.right)

    # average O(lgn) space (worst case O(n) space), iteratively, one-pass
    def recoverTree2(self, root):
        res, stack, first, second = None, [], None, None
        while True:
            while root:
                stack.append(root)
                root = root.left
            if not stack:
                break
            node = stack.pop()
            # first time occurs reversed order
            if res and res.val > node.val:
                if not first:
                     first = res
                # first or second time occurs reversed order
                second = node
            res = node
            root = node.right
        first.val, second.val = second.val, first.val