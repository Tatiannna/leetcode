# 3216. Lexicographically Smallest String After a Swap

# todo

class Solution:
    def getSmallestString(self, s: str) -> str:

        res = s

        for i in range(1, len(s)):
            if int(s[i-1]) > int(s[i]):
                res = s[0:i-1] + s[i] + s[i-1] + s[i+1:]
                return res
           
        return res