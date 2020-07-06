class Solution:
    def Fibonacci(self, n: int):
        if n <= 0:
            return 0
        if n == 1 or n == 2:
            return 1
        return self.Fibonacci(n-2)+self.Fibonacci(n-1)

    def Fibonacci1(self, n: int):
        if n <= 0:
            return 0
        if n == 1 or n == 2:
            return 1
        first, second, third = 1, 1, 0
        for i in range(3, n+1):
            third = first + second
            first, second = second, third
        return third


sol = Solution()
print(sol.Fibonacci(10))
