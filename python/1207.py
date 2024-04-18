# 1207. Unique Number of Occurrences

# Given an array of integers arr, return true if the number of occurrences of each value in the array is unique or false otherwise.

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        occs = set()
        dic = {}

        for num in arr:
            if num not in dic:
                dic[num] = 1
            else:
                dic[num] += 1
        
        for val in dic.values():
            if val not in occs:
                occs.add(val)
            else:
                return False

        return True