# 15. 3Sum


# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

# Notice that the solution set must not contain duplicate triplets.


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        ans = []
        nums.sort()
        a, l, r = 0, 1, len(nums) - 1

        while a < len(nums) - 2:
            while l < r:
                if nums[a] + nums[l] + nums[r] == 0:
                    # if [nums[a], nums[l], nums[r]] not in ans:
                    ans.append( [nums[a], nums[l], nums[r]] )
                    l += 1
                    while(nums[l] == nums[l-1] and l < r):
                        l+=1
                elif nums[a] + nums[l] + nums[r] < 0:
                    l += 1
                else:
                    r -= 1
            a += 1

            while 0 < a < len(nums)-2 and nums[a-1] == nums[a]:
                a += 1
            l = a + 1
            r = len(nums) -1
        return ans