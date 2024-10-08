# 3300. Minimum Element After Replacement With Digit Sum

class Solution:
    def minElement(self, nums: List[int]) -> int:
        res = float(inf)

        for i in range(len(nums)):
            replacement = 0
            for digit in str(nums[i]):
                replacement += int(digit)
            nums[i] = replacement
            res = min(res, replacement)

        return res  