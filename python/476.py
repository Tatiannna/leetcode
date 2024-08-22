# 476. Number Complement
# https://leetcode.com/problems/number-complement/description/?envType=daily-question&envId=2024-08-22

class Solution:
    def findComplement(self, num: int) -> int:
        s = bin(num)[2:]
        res = ''

        for c in s:
            res += '1' if c =='0' else '0'
        return int(res, 2)