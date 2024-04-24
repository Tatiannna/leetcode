# 977. Squares of a Sorted Array

# Given an integer array nums sorted in non-decreasing order, 
# return an array of the squares of each number sorted in non-decreasing order.


# Follow up: Squaring each element and sorting the new array is very trivial, 
# could you find an O(n) solution using a different approach?

# todo

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        ans = []

        low = 0
        high = len(nums) -1

        for i in range(len(nums)):
            if nums[i] <= 0:
                low = i


        for i in range(len(nums)):
            if nums[i] > 0:
                high = i
                break

        while low >= 0 and high < len(nums):
            if abs(nums[low]) <= abs(nums[high]):
                ans.append(nums[low] ** 2)
                low -= 1
            else:
                ans.append(nums[high] **2)
                high += 1
        
        if low < 0:
            for i in range(high, len(nums)):
                ans.append(nums[i] ** 2)
        else:
            for i in range(low, -1, -1):
                ans.append(nums[i] ** 2)


        return ans 