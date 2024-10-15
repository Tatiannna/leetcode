# 1422. Maximum Score After Splitting a String


class Solution:
    def maxScore(self, s: str) -> int:
        
        res = 0

        for i in range(1, len(s)):
            score = s[0:i].count('0') + s[i:].count('1')
            res = max(score, res)

        return res