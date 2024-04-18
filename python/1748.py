# 1748. Sum of Unique Elements

# You are given an integer array nums. The unique elements of an array are the elements that appear exactly once in the array.

# Return the sum of all the unique elements of nums.

class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        els = {}

        for num in nums:
            if num not in els:
                els[num] = 1
            else:
                els[num] += 1
        
        sum = 0

        for el in els:
            if els[el] == 1:
                sum += el

        return sum