# 1323. Maximum 69 Number

# You are given a positive integer num consisting only of digits 6 and 9.

# Return the maximum number you can get by changing at most one digit (6 becomes 9, and 9 becomes 6).


class Solution:
    def maximum69Number (self, num: int) -> int:
        n = list(str(num))

        for i in range(0, len(n)):
            if n[i] == '6':
                print("found 6!")
                n[i] = '9'
                break
                
        return int(''.join(n))