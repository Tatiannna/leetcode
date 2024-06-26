
# 3146. Permutation Difference between Two Strings



# You are given two strings s and t such that every character occurs at most once in s and t is a permutation of s.

# The permutation difference between s and t is defined as the sum of the absolute difference between the index of the occurrence of each character in s and the index of the occurrence of the same character in t.

# Return the permutation difference between s and t.


class Solution:
    def findPermutationDifference(self, s: str, t: str) -> int:
        tot = 0

        for i in range(len(s)):
            tot += abs(i - t.index(s[i]))
        return tot