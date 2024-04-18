# 2206. Divide Array Into Equal Pairs

# You are given an integer array nums consisting of 2 * n integers.

# You need to divide nums into n pairs such that:

# Each element belongs to exactly one pair.
# The elements present in a pair are equal.
# Return true if nums can be divided into n pairs, otherwise return false.


class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        dic = {}

        for num in nums:
            if num not in dic:
                dic[num] = 1
            else:
                dic[num] += 1

        for val in dic.values():
            if val % 2 == 1:
                return False

        return True