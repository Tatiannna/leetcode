class Solution:
    def pivotInteger(self, n: int) -> int:

        low = 1
        high = n
        ans = -1
        sum_left = 1
        sum_right = n

        while low <= high:
            if sum_left == sum_right:
                return low
            elif sum_right > sum_left:
                low += 1
                sum_left += low
            else:
                high -=1
                sum_right += high
        return -1
        