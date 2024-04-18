# 1941. Check if All Characters Have Equal Number of Occurrences

# Given a string s, return true if s is a good string, or false otherwise.

# A string s is good if all the characters that appear in s have the same number of occurrences (i.e., the same frequency).


class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        occs = {}
        
        for c in s:
            if c not in occs:
                occs[c] = 1
            else:
                occs[c] += 1

        num = occs[s[0]]
        for val in occs.values():
            if val != num:
                return False

        return True