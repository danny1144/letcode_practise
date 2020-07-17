#
# @lc app=leetcode.cn id=4 lang=python3
#
# [4] 寻找两个正序数组的中位数
#

# @lc code=start
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
         
        lst=nums1.extends(nums2)
        lst.sort()
        s1=len(lst)
        if s1%2 != 0:
            return lst[s1//2-1]
        return lst[s1]



# @lc code=end
