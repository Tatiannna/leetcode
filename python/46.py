class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        ans = []
        queue = [nums]
        s = {nums}

        while queue:
            current = queue.pop()
            arr = []

            for num in nums:
                while len(arr) < len(nums):



            