# 347. Top K Frequent Elements

# Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.



class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}
        # freq = [[]] * len(nums)
        freq = [ [] for i in range(len(nums) + 1)]
        solution = []
        

        for num in nums:
            if num in counts:
                counts[num] += 1
            else:
                counts[num] = 1

        for key in counts:
            freq[counts[key]].append(key)
        
        print(freq)
        for i in range(len(freq) -1, 0, -1):
            for num in freq[i]:
                solution.append(num)
                if (len(solution) == k):
                    return solution