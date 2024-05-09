# 2553. Separate the Digits in an Array

# Given an array of positive integers nums, return an array answer that consists of the digits of each integer in nums after separating them in the same order they appear in nums.

# To separate the digits of an integer is to get all the digits it has in the same order.

# For example, for the integer 10921, the separation of its digits is [1,0,9,2,1].

# todo


class Solution:
    def minOperations(self, nums: List[int]) -> int:

        count = 0

        for i in range(1, len(nums)):
            if nums[i-1] >= nums[i]:
                val = nums[i-1] - nums[i] + 1
                count += val
                nums[i] += val

        return count
        