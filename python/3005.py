# 3005. Count Elements With Maximum Frequency

# You are given an array nums consisting of positive integers.

# Return the total frequencies of elements in nums such that those elements all have the maximum frequency.

# The frequency of an element is the number of occurrences of that element in the array.

class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        freq = {}
        max = 1

        for num in nums:
            if num not in freq:
                freq[num] = 1
            else:
                freq[num] += 1
                max = freq[num] if freq[num] > max else max

        count = 0
        for val in freq.values():
            if val == max:
                count += 1

