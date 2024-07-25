
# 128. Longest Consecutive Sequence

# Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

# You must write an algorithm that runs in O(n) time.



class Solution:

    # initial solution
    # def longestConsecutive(self, nums: List[int]) -> int:
    #     ans = 1
    #     current = 1

    #     if len(nums) == 0:
    #         return 0

    #     nums.sort()
    #     current = 1
    #     for i in range(1, len(nums)):
    #         if nums[i-1] + 1 == nums[i]:
    #             current += 1
    #         elif nums[i-1] == nums[i]:
    #             continue
    #         else:
    #             current = 1
    #         ans = current if current > ans else ans
    #     return ans  




        class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        # other solution (works but times out)
        # if len(nums) == 0:
        #     return 0

        # max_ = max(nums)
        # min_ = min(nums)
        # s = set()

        # longest = 1
        # current = 0

        # for num in nums:
        #     s.add(num)


        # for i in range(min_, max_ + 1):
        #     if i in s:
        #         current += 1
        #         longest = current if current > longest else longest
        #     elif current != 0:
        #         current = 0
        # return longest


        # best solution

        
        if len(nums) == 0:
            return 0

        s = set(nums)
        longest = 1
        
        for num in s:
            current = 1
            if num - 1 not in s: 
                n = num + 1
                while n in s:
                    current += 1
                    longest = max(current, longest)
                    n += 1
        return longest