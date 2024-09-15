# 509. Fibonacci Number
# https://leetcode.com/problems/fibonacci-number/description/


class Solution:
    def fib(self, n: int) -> int:

        if n == 1 or n == 0:
            return n

        dp = defaultdict(int)
        dp[1] = 1

        a = 2
        while a <= n:
            dp[a] = dp[a-1] + dp[a-2]
            a += 1

        return dp[n]