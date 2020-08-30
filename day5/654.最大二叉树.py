# @before-stub-for-debug-begin
from python3problem654 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode.cn id=654 lang=python3
#
# [654] 最大二叉树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> TreeNode:
        if not nums:
            return None
        maxi=max(nums) 
        pos = nums.index(maxi)
        root = TreeNode(maxi)
        root.left=self.constructMaximumBinaryTree(nums[0:pos])
        root.right=self.constructMaximumBinaryTree(nums[pos+1:])
        return root

        
# @lc code=end

