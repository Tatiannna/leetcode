# 2485. Find the Pivot Integer


# Given a positive integer n, find the pivot integer x such that:

# The sum of all elements between 1 and x inclusively equals the sum of all elements between x and n inclusively.
# Return the pivot integer x. If no such integer exists, return -1. It is guaranteed that there will be at most one pivot index for the given input.



class Solution:
    def pivotInteger(self, n: int) -> int:

        low = 1
        high = n
        sum_left = 1
        sum_right = n

        while low <= high:
            if low == high and sum_left == sum_right:
                return low
            elif sum_right > sum_left:
                low += 1
                sum_left += low
            else:
                high -=1
                sum_right += high
        return -1
        