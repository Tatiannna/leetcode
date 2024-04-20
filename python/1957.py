# 1957. Delete Characters to Make Fancy String

# A fancy string is a string where no three consecutive characters are equal.

# Given a string s, delete the minimum possible number of characters from s to make it fancy.

# Return the final string after the deletion. It can be shown that the answer will always be unique.


class Solution:
    #todo
    def makeFancyString(self, s: str) -> str:

        start = 0
        lst = (list(s))

        while start <= len(lst) -3:
            if len(set(lst[start:start+3])) == 1:
                lst.pop(start)
            else:
                start += 1
        return ''.join(lst)
        