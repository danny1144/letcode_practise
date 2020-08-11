#
# @lc app=leetcode.cn id=169 lang=python3
#
# [169] 多数元素
#

# @lc code=start


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        from collections import Counter

        zsize = len(nums) // 2

        aout = Counter(nums).most_common(1)

        for i, v in list(aout):
            if v > zsize:
                return i
        return None
# @lc code=end
