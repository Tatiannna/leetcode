
from collections import deque

# todo

class Solution:

    def word_letter_transformation(self, start, end, word_list):

        count = 0
        queue = deque([start])
        visited = {start}

        while queue:
            current = queue.popleft()
            l = len(queue)

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
                            print(f'found a transformation! current: {current} new: {word}')
                            queue.append(word)
                            visited.add(word)
            count += 1 if len(queue) > l else 0

        return count

word1 = 'hit'
word2 = 'cog'
wlist = ['hot', 'dot', 'dog', 'lot', 'log', 'cog']

sol = Solution()

print(sol.word_letter_transformation(word1, word2, wlist))