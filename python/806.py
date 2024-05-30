# 806. Number of Lines To Write String

# You are given a string s of lowercase English letters and an array widths denoting how many pixels wide each lowercase English letter is. Specifically, widths[0] is the width of 'a', widths[1] is the width of 'b', and so on.

# You are trying to write s across several lines, where each line is no longer than 100 pixels. Starting at the beginning of s, write as many letters on the first line such that the total width does not exceed 100 pixels. Then, from where you stopped in s, continue writing as many letters as you can on the second line. Continue this process until you have written all of s.

# Return an array result of length 2 where:

# result[0] is the total number of lines.
# result[1] is the width of the last line in pixels.


# todo 

class Solution:
    def numberOfLines(self, widths: List[int], s: str) -> List[int]:
        dic = {'a': 0, 'b': 1, 'c': 2, 'd': 3,'e': 4, 'f': 5, 'g': 6, 'h': 7,'i': 8, 'j': 9, 'k': 10, 'l': 11, 'm': 12, 'n': 13 ,'o': 14, 'p': 15,'q': 16, 'r': 17,'s': 18, 't': 19,'u': 20, 'v': 21,'w': 22, 'x': 23,'y': 24, 'z': 25}
    
        tot = 0

        for c in s:
            tot += widths[dic[c]]

        lines = tot // 100 + 1
        last = tot % lines
        last_index = len(s) - 1 - last
        width = 0

        for i in range(last_index, len(s)):
            width += dic[s[i]]

        return [lines, width]