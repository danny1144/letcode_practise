#
# @lc app=leetcode.cn id=104 lang=python3
#
# [104] 二叉树的最大深度
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0
        list = [root]
        deepth = 0
        while len(list):
            size = len(list)
            deepth += 1
            while size > 0:
                cur = list.pop(0)
                if cur.left:
                    list.append(cur.left)
                if cur.right:
                    list.append(cur.right)
                size = size - 1
            
        return deepth
# @lc code=end
