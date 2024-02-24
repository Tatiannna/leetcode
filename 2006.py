# 2006. Count Number of Pairs With Absolute Difference K

# Given an integer array nums and an integer k, return the number of pairs (i, j) where i < j such that |nums[i] - nums[j]| == k.

# The value of |x| is defined as:

# x if x >= 0.
# -x if x < 0.


# https://leetcode.com/problems/count-number-of-pairs-with-absolute-difference-k/




class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        
        count = 0
        mydict = {}
        
        for i in range(len(nums)):
            mydict[nums[i]] = True
            if( (k + nums[i]) in mydict.keys()  or (-k + nums[i]) in mydict.keys() ):
                count += 1

        return count