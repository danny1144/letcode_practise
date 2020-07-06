#
# @lc app=leetcode.cn id=215 lang=python3
#
# [215] 数组中的第K个最大元素
#
# @lc code=start


class Solution:
    # def findKthLargest(self, nums: List[int], k: int) -> int:
    #     size = len(nums)
    #     nums.sort()
    #     return nums[size-k]
    def findKthLargest(self, nums: List[int], k: int) -> int:
        q = []
        for c in nums:
            heapq.heappush(q, c)
            while len(q) > k:
                heapq.heappop(q)
        return heapq.heappop(q)

# @lc code=end
