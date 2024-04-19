
# 1704. Determine if String Halves Are Alike

# You are given a string s of even length. Split this string into two halves of equal lengths, and let a be the first half and b be the second half.

# Two strings are alike if they have the same number of vowels ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'). Notice that s contains uppercase and lowercase letters.

# Return true if a and b are alike. Otherwise, return false.


class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
        count1 = count2 = 0

        for i in range(len(s)):
            if s[i] in vowels:
                if i >= len(s)/2:
                    count2 += 1
                elif i < len(s)/2:
                    count1 += 1
        return count1 == count2 