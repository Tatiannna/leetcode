# 3258. Count Substrings That Satisfy K-Constraint I


class Solution:
    def countKConstraintSubstrings(self, s: str, k: int) -> int:

        l = 0
        r = 0
        res = 0

        while r < len(s):
            sub = s[l:r+1]
            while sub.count('0') <= k and sub.count('1') <= k:
                res += 1
                r += 1
            if sub.count('0') > k and l <= r:
                while l != '0':
                    l +=1
            if sub.count('1') > k and l <= r:
                 while l != '1':
                    l += 1

        return res