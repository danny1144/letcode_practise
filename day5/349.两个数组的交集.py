#
# @lc app=leetcode.cn id=349 lang=python3
#
# [349] 两个数组的交集
#

# @lc code=start
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        lst = []
        nums1.sort()
        nums2.sort()
        p, q = 0, 0
        while nums1 and nums2 and p < len(nums1) and q < len(nums2):
            if nums1[p] == nums2[q]:
                lst.append(nums1[p])
                p, q = p+1, q+1
                continue
            if nums1[p] > nums2[q]:
                q = q+1
            else:
                p = p+1
        return set(lst)
# @lc code=end
