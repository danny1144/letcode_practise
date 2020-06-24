# 给定 nums = [2, 7, 11, 15], target = 9
class Solution:
    def twoSum(self, nums, target):
        hashmap = {}
        for k, v in enumerate(nums):
            if target-v in hashmap:
                return [hashmap[target-v], k]
            hashmap[v] = k
# 利用字典存储遍历的数值与索引，一边遍历一边查询，效率较高
