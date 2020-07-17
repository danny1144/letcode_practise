class Solution:
    def fab(self, n):
        if n == 0 or n == 1:
            return 1
        return self.fab(n-1)+self.fab(n-2)

    def findRepeatNumber(self, nums) -> int:
        lst = [nums[0]]
        for i in range(1, len(nums)):
            if lst.count(nums[i]) >= 1:
                return nums[i]
            lst.append(nums[i])
        return -1

    def findRepeatNumber1(self, nums) -> int:
        pre = nums[0]
        for i in range(1, len(nums)):
            if pre == nums[i]:
                return nums[i]
            pre = nums[i]


sol = Solution()
print(sol.findRepeatNumber1([1, 2, 3, 4, 5, 3, 2, 2, 1]))
