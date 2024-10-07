


class Solution:
    def kthCharacter(self, k: int) -> str:
        word = 'a'

        while len(word) < k :
            word += str(ord(word[len(word) -1 ]))


        return word[k - 1]
        