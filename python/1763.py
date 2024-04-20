# 1763. Longest Nice Substring

# A string s is nice if, for every letter of the alphabet that s contains, it appears both in uppercase and lowercase. For example, "abABB" is nice because 'A' and 'a' appear, and 'B' and 'b' appear. However, "abA" is not because 'b' appears, but 'B' does not.

# Given a string s, return the longest substring of s that is nice. If there are multiple, return the substring of the earliest occurrence. If there are none, return an empty string.


class Solution:
    # todo
    def longestNiceSubstring(self, s: str) -> str:
        longest = ''
        left = 0
        right = 1

        while right < len(s):
            # if substring nice increase right
            # if len > longest, reassign
            
            while (right < len(s) and s[left].upper() in s[left:right+1] and 
                s[left].lower() in s[left:right+1] and s[right].upper() in s[left:right+1] 
                and s[right].lower() in s[left:right+1]):

                longest = s[left:right+1] if right - left + 1 > len(longest) else longest
                right +=1
                
            left = right
            right = left + 1
            
        return longest   