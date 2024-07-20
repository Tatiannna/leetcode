# 3190. Find Minimum Operations to Make All Elements Divisible by Three

# You are given an integer array nums. In one operation, you can add or subtract 1 from any element of nums.

# Return the minimum number of operations to make all elements of nums divisible by 3.


class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        count = 0

        for num in nums:
            count += 1 if num % 3 != 0 else 0

        return count