#  >给定一个**非空**整数数组，除了某个元素只出现一次以外，其余每个元素均出现两次。找出那个只出现了一次的元素。

class Solution():

    def singleNumber(self, n):
        x = 0
        for k, v in enumerate(n):
            x = x ^ v
        return x, k


x = Solution()
print(x.singleNumber([1, 2, 3, 2, 3, 1, 5, 6, 6, 5, 4]))
