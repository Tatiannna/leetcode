# 1119. Remove Vowels from a String

class Solution:
    def removeVowels(self, s: str) -> str:
        chars = {'a', 'e', 'i', 'o', 'u'}
        res = ''

        for c in s:
            if c not in chars:
                res += c
        return res