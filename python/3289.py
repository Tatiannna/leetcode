# 3289. The Two Sneaky Numbers of Digitville

class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        n = defaultdict(int)
        res = []

        for num in nums:
            n[num] += 1
            if n[num] == 2:
                res.append(num)
                if len(res) == 2:
                    return res