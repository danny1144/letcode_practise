#
# @lc app=leetcode.cn id=125 lang=python3
#
# [125] 验证回文串
#

# @lc code=start
from day3.deque import Deque


class Solution:
    def isPalindrome(self, s: str) -> bool:
        result = True
        q = Deque()
        for i in s:
            q.addFront(i)
        while q.size() > 1:
            if q.removeFront() != q.removeRear():
                result = False
                break
        return result


soltion = Solution()

print(soltion.isPalindrome("121"))


# @lc code=end
