# 3110. Score of a String

# You are given a string s. The score of a string is defined as 
# the sum of the absolute difference between the ASCII values of adjacent characters.

# Return the score of s.


class Solution:
    def scoreOfString(self, s: str) -> int:
        ans = 0
        i = 0

        while i < len(s) -1 :
            print(abs(ord(s[i])))
            ans += abs(ord(s[i]) - ord(s[i+1]))

            i += 1

        return ans