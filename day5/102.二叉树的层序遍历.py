# @before-stub-for-debug-begin
from python3problem102 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode.cn id=102 lang=python3
#
# [102] 二叉树的层序遍历
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        res = []
        if root is None:
            return res
        queue = [root]
        while len(queue):
            size = len(queue)
            p = []
            for _ in range(size):
                node = queue.pop(0)
                p.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            res.append(p)
        return res


# @lc code=end
# 二叉树的层次遍历

# 1需要借助队列实现，每次遍历二叉树的时候，把每一层的数据放在队列里面
# 队列会按照先进先出的顺序进行出队。
# 没遍历一层，就把结果赋值给大的集合，
# 通过迭代就能获取结果
