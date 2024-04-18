# 1684. Count the Number of Consistent Strings


# You are given a string allowed consisting of distinct characters and an array of strings words. A string is consistent if all characters in the string appear in the string allowed.

# Return the number of consistent strings in the array words.


class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        count = 0

        for word in words:
            for i in range(len(word)):
                if word[i] not in allowed:
                    break
                elif i == len(word) -1:
                    count += 1

        return count



