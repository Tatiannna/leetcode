# 3099. Harshad Number

# An integer divisible by the sum of its digits is said to be a Harshad number. 
# You are given an integer x. Return the sum of the digits of x if x is a Harshad number, otherwise, return -1.


class Solution:
    def sumOfTheDigitsOfHarshadNumber(self, x: int) -> int:
        n = str(x)
        sums = 0

        for c in n:
            sums += int(c)

        return sums if x % sums == 0 else -1   