# 238. Product of Array Except Self

# Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

# You must write an algorithm that runs in O(n) time and without using the division operation.


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        solution = []
        prefix = []
        postfix = [1] * len(nums)

        # postfix = [1 for i in range(len(nums))]
        prod = 1

        for i in range(0, len(nums)):
            prod *= nums[i]
            prefix.append(prod)

        prod = 1

        for i in range(len(nums) - 1, -1, -1):
            prod *= nums[i]
            postfix[i] = prod

        for i in range(0, len(nums)):
            if i == 0:
                solution.append(postfix[i+1])
            elif i < len(nums) -1:
                solution.append(prefix[i-1] * postfix[i+1])
            else:
                solution.append(prefix[i-1])
        return solution