# 2894. Divisible and Non-divisible Sums Difference

# You are given positive integers n and m.

# Define two integers, num1 and num2, as follows:

# num1: The sum of all integers in the range [1, n] that are not divisible by m.
# num2: The sum of all integers in the range [1, n] that are divisible by m.
# Return the integer num1 - num2.


class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        num1 = num2 = 0

        for i in range(1, n+1):
            num1 += i if i % m != 0 else 0
            num2 += i if i % m == 0 else 0
        return num1 - num2
        