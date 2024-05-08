# 387. First Unique Character in a String

# Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.


class Solution:
    def firstUniqChar(self, s: str) -> int:
        letters = {}

        for i in range(len(s)):
            if s[i] in letters:
                letters[s[i]].append(i)
            else:
                letters[s[i]] = [i]

        for c in letters:
            if len(letters[c]) == 1:
                return letters[c][0]
        

        return -1
        