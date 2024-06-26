
# 1832. Check if the Sentence Is Pangram


# A pangram is a sentence where every letter of the English alphabet appears at least once.

# Given a string sentence containing only lowercase English letters, return true if sentence is a pangram, or false otherwise.



class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        ans = 'abcdefghijklmnopqrstuvwxyz'

        for c in sentence:
            if c in ans:
                ans = ans.replace(c, '')

        return len(ans) == 0