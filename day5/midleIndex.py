#   寻找数组的中心索引

class Solution:
    def find(self, nums: [int]):
        right = 0
        for i in nums:
            right += i
        left = 0
        for index in range(len(nums)):
            right = right - nums[index]
            if index != 0:
                left = left + nums[index-1]
            if left == right:
                return index

        return -1


solution = Solution()
print(solution.find([1, 4, 6, 6, 7, 9, 4, 4]))
