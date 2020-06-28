# 在一个长度为 n 的数组里的所有数字都在 0 到 n-1 的范围内。数组中某些数字是重复的，但不知道有几个数字是重复的，
# 也不知道每个数字重复几次。请找出数组中任意一个重复的数字。

class Solution():
    def duplicate(self, numbers, duplication):
        long = len(numbers)
        for i in range(len(numbers)):
            index = numbers[i] % long if numbers[i] >= long else numbers[i]
            if numbers[index] > long:
                duplication.append(index)
                return True
            numbers[index] += long
        return False

    def findRepeat(self, numbers=[], duplication=[]):
        if not numbers:
            return False
        numbers.sort()
        for i in range(1, len(numbers)):
            if numbers[i] == numbers[i-1]:
                duplication.append(numbers[i])
                return True

        return False


if __name__ == "__main__":
    sol = Solution()
    list = [1, 2, 4, 5, 2, 4]
    dum = []
    sol.findRepeat(list, dum)
    print(dum)
