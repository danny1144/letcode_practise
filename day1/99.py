class Solution:
    def multiply99(self):
        for i in range(1, 10):
            for j in range(1, i+1):
                print('%d * %d =%d' % (j, i, i*j), end='\t')
            print('\r\n')


sol = Solution()
sol.multiply99()