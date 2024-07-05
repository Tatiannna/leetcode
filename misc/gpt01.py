
from collections import deque

# todo

class Solution:

    def word_letter_transformation(self, start, end, word_list):

        if start == end:
            return 0

        count = 1
        queue = deque([start])
        visited = {start}

        while queue:
            l = len(queue)

            for i in range(l):
                current = queue.popleft()

                for word in word_list:
                    if end == current:
                        return count
                    else:
                        if len(word) == len(current):
                            diff_count = 0
                            for i in range(len(current)):
                                if current[i] != word[i]:
                                    diff_count += 1
                                if diff_count > 1:
                                    break

                            if diff_count == 1 and word not in visited:
                                # print(f'found a transformation! current: {current} new: {word}')
                                queue.append(word)
                                visited.add(word)
            # count += 1 if len(queue) > l else 0
            count += 1
        return 0

# word1 = 'hit'
# word2 = 'cog'
# wlist = ['hot', 'dot', 'dog', 'lot', 'log', 'cog']

solution = Solution()

# print(sol.word_letter_transformation(word1, word2, wlist))

print(solution.word_letter_transformation("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]))  # Expected output: 5
print(solution.word_letter_transformation("hit", "cog", ["hot", "dot", "dog", "lot", "log"]))  # Expected output: 0 (no transformation possible)
print(solution.word_letter_transformation("hit", "hit", ["hot", "dot", "dog", "lot", "log", "cog"]))  # Expected output: 0 (start and end are the same)
print(solution.word_letter_transformation("a", "c", ["a", "b", "c"]))  # Expected output: 2
print(solution.word_letter_transformation("abc", "xyz", ["abd", "acd", "axy", "xyz"]))  # Expected output: 0 (no valid transformation sequence)