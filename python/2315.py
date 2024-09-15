# 2315. Count Asterisks

# https://leetcode.com/problems/count-asterisks/description/



class Solution:
    def countAsterisks(self, s: str) -> int:
        res = s.split('|')
        count = 0

        for st in res:
            for c in st:
                count += 1 if c =='*' else 0

        return count