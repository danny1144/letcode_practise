#
# @lc app=leetcode.cn id=94 lang=python3
#
# [94] 二叉树的中序遍历
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        lst = []
        self.help(root, lst)
        return lst

    def help(self, node: TreeNode, lst: []):
        if node:
            if node.left:
                self.help(node.left, lst)
            lst.append(node.val)
            if node.right:
                self.help(node.right, lst)

# @lc code=end
