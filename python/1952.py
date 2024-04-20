# 1952. Three Divisors

# Given an integer n, return true if n has exactly three positive divisors. Otherwise, return false.

# An integer m is a divisor of n if there exists an integer k such that n = k * m.

class Solution:
    def isThree(self, n: int) -> bool:
        count = 2

        if n < 4:
            return False
        else:
            for i in range(2, n // 2+1):
                if n % i == 0:
                    count += 1
                    if count == 4:
                        return False

        return count == 3