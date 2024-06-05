
# 2053. Kth Distinct String in an Array


# A distinct string is a string that is present only once in an array.

# Given an array of strings arr, and an integer k, return the kth distinct string present in arr. If there are fewer than k distinct strings, return an empty string "".

# Note that the strings are considered in the order in which they appear in the array.



class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:

        count = 0
        d = {}

        for num in arr:
            if num not in d:
                d[num] = 1
            else:
                d[num] +=1

        for key in d:
            if d[key] == 1:
                count +=1
            if count == k:
                return key

        return ''