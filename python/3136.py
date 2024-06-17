
# 3136. Valid Word

# A word is considered valid if:

# It contains a minimum of 3 characters.
# It contains only digits (0-9), and English letters (uppercase and lowercase).
# It includes at least one vowel.
# It includes at least one consonant.
# You are given a string word.

# Return true if word is valid, otherwise, return false.

# todo
class Solution:
    def isValid(self, word: str) -> bool:
        nums = '0123456789'
        cons = 'bcdfghjklmnpqrstvwxyz'
        vowels = 'aeiou'

        vcount = 0
        ccount = 0
        if len(word) >= 3:
            for c in word:
                if c.lower() in vowels:
                    vcount += 1
                elif c.lower() in cons:
                    ccount += 1
                else:
                    if c not in nums:
                        return False
        else:
            return False

        return True if vcount > 0 and ccount > 0 else False