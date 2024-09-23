# 386. Lexicographical Numbers
# https://leetcode.com/problems/lexicographical-numbers/?envType=daily-question&envId=2024-09-21


class Solution:
    def lexicalOrder(self, n: int) -> List[int]:

        arr = []

        for i in range(1, n + 1):
            arr.append(str(i))

        arr.sort()
        for i in range(len(arr)):
            arr[i] = int(arr[i])

        return arr   