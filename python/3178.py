
# 3178. Find the Child Who Has the Ball After K Seconds

# You are given two positive integers n and k. There are n children numbered from 0 to n - 1 standing in a queue in order from left to right.

# Initially, child 0 holds a ball and the direction of passing the ball is towards the right direction. After each second, the child holding the ball passes it to the child next to them. Once the ball reaches either end of the line, i.e. child 0 or child n - 1, the direction of passing is reversed.

# Return the number of the child who receives the ball after k seconds.


# todo

class Solution:
    def numberOfChild(self, n: int, k: int) -> int:
        # at second 1, ball will be on nums[1]
        # at second n, ball will be on nums[n - 1]

        # get remainder of k / n

        # depending on whether k // n was odd or even remainder will be
        # traveled from left end or right end

        # if k // n is odd, we'll count from right to remainder
        # else, count from left n[0] to remainder


        # at second 

        div = k // n
        rem = k % n


        if div % 2 == 0:
            return rem
        else:
            return n - 1 - rem
        