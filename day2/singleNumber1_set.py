#
# @lc app=leetcode.cn id=137 lang=python3
#
# [137] 只出现一次的数字 II
#

# @lc code=start
class Solution:
    def singleNumber(self, nums):
        return (3*sum(set(nums))-sum(nums))//2
# @lc code=end


# 使用dict完成重复数字的计数
# 使用set集合公式 3*(a+b+c)-(a+a+a+b+b+b+c)=2c
