class Solution:
    def sum(self, n):
        return n and (n + self.sum(n-1))
    # 不使用四则运算做加法

    def Add(self, a, b):
        return a if b == 0 else self.Add(a ^ b, (a & b) << 1)


if __name__ == "__main__":
    sol = Solution()
    print(sol.sum(100))
    print(sol.Add(100, 124))
# 使用递归解法最重要的是指定返回条件指定返回条件，但是本题无法直接使用 if 语句来。
# 条件与 && 具有短路原则，即在第一个条件语句为 false 的情况下不会去执行第二个条件语句。利用这一特性，
# 将递归的返回条件取非然后作为 && 的第一个条件语句，递归的主体转换为第二个条件语句，那么当递归的返回条件为 true
# 的情况下就不会执行递归的主体部分，递归返回。
