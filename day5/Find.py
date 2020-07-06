# 二维数组，行从左到右有序递增，列从上至下有序递增。查找整数是否在二维数组中

class Solution:
    def find(self, arr=[[int]], k=int):
        row = int(len(arr)) - 1
        columns = 0
        while row >= 0 and columns <= int(len(arr[0])):
            if arr[row][columns] > k:
                row = row - 1
            elif arr[row][columns] < k:
                columns = columns + 1
            else:
                return True
        return False


sol = Solution()
print(sol.find([[1, 2, 3, 4], [2, 3, 4, 5], [3, 4, 5, 6], [4, 5, 6, 7]], 3))
