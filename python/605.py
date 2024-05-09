
# 605. Can Place Flowers

# You have a long flowerbed in which some of the plots are planted, and some are not. However, flowers cannot be planted in adjacent plots.

# Given an integer array flowerbed containing 0's and 1's, where 0 means empty and 1 means not empty, and an integer n, return true if n new flowers can be planted in the flowerbed without violating the no-adjacent-flowers rule and false otherwise.

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:

        if n > 0 :
            if len(flowerbed) == 1:
                if flowerbed[0] == 0:
                    n -= 1
            else:
                for i in range(0, len(flowerbed)):
                    if n == 0:
                        break
                    elif i == 0 and flowerbed[i] == 0 and flowerbed[i+1] == 0:
                        flowerbed[i] = 1
                        n -= 1
                    elif i > 0 and i < len(flowerbed)-1:
                        if (flowerbed[i] == 0 and flowerbed[i-1] == 0 and flowerbed[i+1] == 0):
                            flowerbed[i] = 1
                            n -= 1 
                    elif i == len(flowerbed) - 1 and flowerbed[i] == 0 and flowerbed[i-1] == 0:
                        flowerbed[i] = 1
                        n -= 1