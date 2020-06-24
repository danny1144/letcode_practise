# 给出一个 32 位的有符号整数，你需要将这个整数中每位上的数字进行反转。

class Solution:
    def reverse(self, x):
        str1 = str(x)
        y = 0
        if '-' in str1:
            y = str1.replace('-', '')
            y = int('-' + y[::-1])
            if y > -2**31 and y < 2**31-1:
                y = y
            else:
                y = 0
        else:
            y = int(str1[::-1])
            if y > -2**31 and y < 2**31-1:
                y = y
            else:
                y = 0
        return y
# 使用字符串反转，然后转成数值 判断边界条件，简洁易懂
