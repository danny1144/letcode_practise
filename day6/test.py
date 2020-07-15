class Solution:
    def fab(self, n):
        if n == 0 or n == 1:
            return 1
        return self.fab(n-1)+self.fab(n-2)


sol = Solution()
print(sol.fab(4))
