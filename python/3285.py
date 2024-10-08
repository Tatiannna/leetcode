# 3285. Find Indices of Stable Mountains

class Solution:
    def stableMountains(self, height: List[int], threshold: int) -> List[int]:
        res = []
        n = False

        for i in range(len(height)):
            if n:
                res.append(i)
                n = False
            if height[i] > threshold:
                n = True
        return res    