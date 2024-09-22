# 2859. Sum of Values at Indices With K Set Bits
# https://leetcode.com/problems/sum-of-values-at-indices-with-k-set-bits/description/


class Solution:
    def sumIndicesWithKSetBits(self, nums: List[int], k: int) -> int:
        res = 0

        for i in range(len(nums)):
            bit_sum = 0
            for bit in bin(i)[2:]:
                if bit == '1':
                    bit_sum += 1

            if bit_sum == k:
                res += nums[i]
        return res