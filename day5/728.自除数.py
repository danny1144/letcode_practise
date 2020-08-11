#
# @lc app=leetcode.cn id=728 lang=python3
#
# [728] 自除数
#

# @lc code=start
class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:

        output = []
        for i in range(left, right+1):
            if '0' not in str(i):
                iList = [int(j) for j in str(i)]
                for j in iList:
                    if i % j != 0:
                        break
                else:
                    output.append(i)
        return output

        # @lc code=end
# ???????0?
# ?????????
# ??????????
