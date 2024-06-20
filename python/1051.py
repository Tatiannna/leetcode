class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        count = 0

        heights2 = copy.copy(heights)
        heights.sort()

        for i in range(len(heights)):
            if heights[i] != heights2[i]:
                count += 1 

        return count
        

        