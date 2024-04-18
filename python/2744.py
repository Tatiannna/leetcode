
# 2744. Find Maximum Number of String Pairs


# You are given a 0-indexed array words consisting of distinct strings.

# The string words[i] can be paired with the string words[j] if:

# The string words[i] is equal to the reversed string of words[j].
# 0 <= i < j < words.length.
# Return the maximum number of pairs that can be formed from the array words.

# Note that each string can belong in at most one pair.

class Solution:
    def maximumNumberOfStringPairs(self, words: List[str]) -> int:
        maps = {}
        count = 0

        for word in words:
            if word[::-1] in maps:
                print(f'the reverse of {word} is already in the dict')
                count += 1
            if word not in maps:
                maps[word] = True

        print(words[0][::-1])
        return count