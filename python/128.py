
# 128. Longest Consecutive Sequence

# Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

# You must write an algorithm that runs in O(n) time.



class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        ans = 1
        current = 1

        if len(nums) == 0:
            return 0

        nums.sort()
        current = 1
        for i in range(1, len(nums)):
            if nums[i-1] + 1 == nums[i]:
                current += 1
            elif nums[i-1] == nums[i]:
                continue
            else:
                current = 1
            ans = current if current > ans else ans
        return ans  