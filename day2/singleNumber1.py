#
# @lc app=leetcode.cn id=137 lang=python3
#
# [137] 只出现一次的数字 II
#

# @lc code=start
class Solution:
    def singleNumber(self, nums):
        hashmap = {}
        for k, v in enumerate(nums):
            hashmap[v] = hashmap.get(v, 0)+1
        for k, v in hashmap.items():
            if v == 1:
                return k
# @lc code=end


# 使用dict完成重复数字的计数
# 使用set集合公式 3*(a+b+c)-(a+a+a+b+b+b+c)=2c
