#
# @lc app=leetcode.cn id=136 lang=python3
#
# [136] 只出现一次的数字
#

# @lc code=start
class Solution:
    def singleNumber(self, n: List[int]) -> int:
        x = 0
        for k, v in enumerate(n):
            x = x ^ v
        return x
