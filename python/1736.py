# 1736. Latest Time by Replacing Hidden Digits


# You are given a string time in the form of  hh:mm, where some of the digits in the string are hidden (represented by ?).

# The valid times are those inclusively between 00:00 and 23:59.

# Return the latest valid time you can get from time by replacing the hidden digits.

class Solution:
    def maximumTime(self, time: str) -> str:
        new_time = ''
	
        if time[0] == '?':
            if time[1] != '?':
                if int(time[1]) > 3:
                    new_time += '1'
                else:
                    new_time += '2'
            else:
                new_time += '2'
        else:
            new_time += time[0]


        if time[1] == '?':
            if int(new_time[0]) < 2:
                new_time += '9'
            else:
                new_time += '3'
        else:
            new_time += time[1]
    
        new_time += ':'

        if time[3] == '?':
            new_time += '5'
        else:
            new_time += time[3]


        if time[4] == '?':
            new_time += '9'
        else:
            new_time += time[4]
        
        return new_time