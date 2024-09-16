# 198. House Robber

# https://leetcode.com/problems/house-robber/description/



class Solution:
    def rob(self, nums: List[int]) -> int:

        dp = [nums[0]]

        if len(nums) < 2:
            return dp[0]
            
        dp.append(max(nums[0], nums[1]))

        for i in range(2, len(nums)):
            dp.append(max(dp[i - 1], nums[i] + dp[i-2]))
        return dp[-1]