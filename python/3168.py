# 3168. Minimum Number of Chairs in a Waiting Room

class Solution:
    def minimumChairs(self, s: str) -> int:

        res = 0
        stack = []

        for c in s:
            if c == 'E':
                stack.append('E')
                res = max(res, len(stack)) 
            else:
                stack.pop()

        return res 