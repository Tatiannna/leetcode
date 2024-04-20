# 1876. Substrings of Size Three with Distinct Characters

# A string is good if there are no repeated characters.

# Given a string s​​​​​, return the number of good substrings of length three in s​​​​​​.

# Note that if there are multiple occurrences of the same substring, every occurrence should be counted.

# A substring is a contiguous sequence of characters in a string.


class Solution:
    def countGoodSubstrings(self, s: str) -> int:

        count = 0
        start = 0

        while start <= len(s) - 3:
            if len(set(s[start:start+3])) == 3:
                count += 1
            start += 1
        return count