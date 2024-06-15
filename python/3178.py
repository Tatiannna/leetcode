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
        