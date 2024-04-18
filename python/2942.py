# 2942. Find Words Containing Character

# You are given a 0-indexed array of strings words and a character x.

# Return an array of indices representing the words that contain the character x.

# Note that the returned array may be in any order.



class Solution:
    def findWordsContaining(self, words: ist[str], x: str) -> List[int]:
        ans = []

        for i in range(len(words)):
            if x in words[i]:
                ans.append(i)
        return ans

print(findWordsContaining(["hello", "world"], 'o'))