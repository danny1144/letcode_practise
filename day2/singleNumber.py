#
# @lc app=leetcode.cn id=136 lang=python3
#
# [136] 只出现一次的数字
#

# @lc code=start
class Solution:
    def singleNumber(self, n: List[int]) -> int:
        x = 0
        if not n:
            return 0
        for v in n:
            x = x ^ v
        return x
