# 860. Lemonade Change

# https://leetcode.com/problems/lemonade-change/description/?envType=daily-question&envId=2024-08-24



class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        change = defaultdict(int)

        for bill in bills:
            if bill == 5:
                change[5] += 1
            elif bill == 10:
                if not change[5]:
                    return False
                else:
                    change[10] += 1
                    change[5] -=1
            else:
                if change[5] and change[10]:
                    change[5] -= 1
                    change[10] -=1
                    change[20] += 1
                elif change[5] >= 3:
                    change[5] -= 3
                else:
                    return False

        return True