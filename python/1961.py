# 1961. Check If String Is a Prefix of Array

# Given a string s and an array of strings words, determine whether s is a prefix string of words.

# A string s is a prefix string of words if s can be made by concatenating the first k strings in words for some positive k no larger than words.length.

# Return true if s is a prefix string of words, or false otherwise.

class Solution:
    def isPrefixString(self, s: str, words: List[str]) -> bool:
        pre = ''
        i = 0

        while i < len(words):
            pre += words[i]
            if s == pre:
                return True
            i += 1
        return False