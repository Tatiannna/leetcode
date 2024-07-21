# 66. Plus One

# You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer. The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading 0's.

# Increment the large integer by one and return the resulting array of digits.

# todo


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        if len(digits) == 1 and digits[0] == 9:
            return [1,0]

        
        i = len(digits) - 1
        digits[i] += 1

        

        while digits[i] > 9:
            digits[i] -= 10
            digits[i-1] += 1
            i -= 1

        return digits

