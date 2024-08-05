# todo

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        
        if len(nums1) == len(nums2):
            nums1 = nums2
        else:
            for i in range(m):
                print(i)
                nums1[i + m] = nums1[i]

            p1 = 0
            p2 = 0
            i = 0

            while i < len(nums1):
                if nums1[p1] < nums2[p2]:
                    nums1[i] = nums1[p1]
                    p1 +=1
                else:
                    nums1[i] = nums2[p2]
                    p2 += 1
                i +=1
