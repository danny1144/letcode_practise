#
# @lc app=leetcode.cn id=101 lang=python3
#
# [101] 对称二叉树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def dfs(self, left, right):
        if not (left or right):
            return True
        if not (left and right):
            return False
        if left.val != right.val:
            return False
        return self.dfs(left.left, right.right) and self.dfs(left.right, right.left)

    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True
        return self.dfs(root.left, root.right)

# @lc code=end
