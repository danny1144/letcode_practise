class Solution:
    def search(self, nums: [int], key: int):

        left = 0
        h = len(nums) - 1
        while left < h:
           # m = left + (h - left) // 2
            m = (left + h) // 2
            if nums[m] >= key:
                h = m
            else:
                left = m+1
        return left


sol = Solution()
print(sol.search([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 1))
