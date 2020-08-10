#
# @lc app=leetcode.cn id=226 lang=python3
#
# [226] 翻转二叉树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        # if root is None:
        #     return root
        # left = self.invertTree(root.left)
        # right = self.invertTree(root.right)
        # root.left = right
        # root.right = left
        # return root
        if root is None:
            return root
        stack = [root]
        while stack:
            cur = stack.pop(-1)
            cur.left, cur.right = cur.right, cur.left
            if cur.left:
                stack.append(cur.left)
            if cur.right:
                stack.append(cur.right)
        return root
# @lc code=end
