
# 205. Isomorphic Strings

# Given two strings s and t, determine if they are isomorphic.
# Two strings s and t are isomorphic if the characters in s can be replaced to get t.
# All occurrences of a character must be replaced with another character while preserving 
# the order of characters. No two characters may map to the same character, but a character 
# may map to itself.

class Solution:
    
    def isIsomorphic(self, s: str, t: str) -> bool:

        ds = {}
        dt = {}

        for i in range(len(s)):

                if s[i] not in ds:
                    ds[s[i]] = [i, 1]
                else:
                    ds[s[i]][1] += 1


                if t[i] not in dt:
                    dt[t[i]] = [i, 1]
                else:
                    dt[t[i]][1] += 1
                
                if ds[s[i]] != dt[t[i]]:
                    return False

        return True  