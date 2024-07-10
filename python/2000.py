
# 2000. Reverse Prefix of Word

# Given a 0-indexed string word and a character ch, reverse the segment of word that starts at index 0 and ends at the index of the first occurrence of ch (inclusive). If the character ch does not exist in word, do nothing.

# For example, if word = "abcdefd" and ch = "d", then you should reverse the segment that starts at 0 and ends at 3 (inclusive). The resulting string will be "dcbaefd".
# Return the resulting string.


# todo

class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:

        i = 0

        while i < len(word):
            if word[i] == ch:
                break
            i += 1
        print(i, word[0:i])
        print(word[i:-1:-1])
        print(word[i:len(word)])



        return word[i:-1:-1] + word[i:len(word)]