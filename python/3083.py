# 3083. Existence of a Substring in a String and Its Reverse

class Solution:
    def isSubstringPresent(self, s: str) -> bool:

        reverse = s[::-1]

        for i in range(1, len(s)):
            if s[i-1:i+1] in reverse:
                return True
        return False