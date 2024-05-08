# 342. Power of Four

# Given an integer n, return true if it is a power of four. Otherwise, return false.

# An integer n is a power of four, if there exists an integer x such that n == 4x.


class Solution:
    def isPowerOfFour(self, n: int) -> bool:

        for i in range(0, n):
            if 4 ** i == n:
                return True
            elif 4 ** i > n:
                break

        return False