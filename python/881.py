# 881. Boats to Save People


# You are given an array people where people[i] is the weight of the ith person, and an infinite number of boats where each boat can carry a maximum weight of limit. Each boat carries at most two people at the same time, provided the sum of the weight of those people is at most limit.

# Return the minimum number of boats to carry every given person.


class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        l, r = 0, len(people) - 1
        ans = 0

        people.sort()
        while l <= r:
            if people[l] == limit:
                l +=1
                ans +=1
            elif people[r] == limit:
                r -=1
                ans += 1
            elif people[l] + people[r] > limit:
                r -= 1
                ans += 1
            elif people[l] + people[r] == limit:
                l += 1
                r -= 1
                ans += 1
            else:
                l +=1
                r -=1
                ans += 1

        return ans