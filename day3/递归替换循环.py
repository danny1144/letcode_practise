class Solution:
    def sum(self, n):
        return n and (n + self.sum(n-1))


if __name__ == "__main__":
    sol = Solution()
    print(sol.sum(100))
