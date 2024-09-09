# 191. Number of 1 Bits
# https://leetcode.com/problems/number-of-1-bits/description/


class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0

        for bit in bin(n)[2:]:
            res += 1 if bit == '1' else 0
        return res


