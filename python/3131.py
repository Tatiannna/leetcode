# 3131. Find the Integer Added to Array I

class Solution:
    def addedInteger(self, nums1: List[int], nums2: List[int]) -> int:

        nums1.sort()
        n = min(nums2)

        return n - nums1[0]