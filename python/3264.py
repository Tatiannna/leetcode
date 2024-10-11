

class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:

        i = 0

        while i < k:
            m = min(nums)
            index = nums.index(m)
            nums[index] *= multiplier

            i += 1

        return nums