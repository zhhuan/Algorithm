"""
File name   : unique_BST2.py
Description : Given an integer n, generate all structurally unique BST's (binary search trees) that store values 1...n.
              For example,
              Given n = 3, your program should return all 5 unique BST's .
Author      : 钟寰
Time        : 2017-01-02 22:28
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        return self.dfs(1,n)

    def dfs(self, start, end):
        if end < start:
            return [None]
        ans = []
        for i in range(start, end + 1):
            ls = self.dfs(start, i - 1)
            rs = self.dfs(i + 1, end)
            for l in ls:
                for r in rs:
                    root = TreeNode(i)
                    root.left = l
                    root.right = r
                    ans.append(root)
        return ans

